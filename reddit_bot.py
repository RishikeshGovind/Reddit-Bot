import praw
import time
import wikipedia
from thefuzz import process

from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
username = os.getenv("username")
password = os.getenv("password")

reddit = praw.Reddit(
    client_id =client_id,
    client_secret = client_secret,
    username = username,
    password = password,
    user_agent = 'test_bot'
)

# Testing subreddit
subreddit = reddit.subreddit("MalayalamMovies")

# Your bot username in lowercase
bot_username = "cocopuffbot"

def get_movie_summary(movie_title):
    try:
        # Step 1: Search "[movie_title] malayalam film"
        search_query = movie_title + " malayalam film"
        search_results = wikipedia.search(search_query)

        # If no results, fallback to just movie title
        if not search_results:
            search_query = movie_title
            search_results = wikipedia.search(search_query)

        if not search_results:
            return f"❌ Couldn't find anything close to **{movie_title}**."

        # Fuzzy match
        best_match, score = process.extractOne(movie_title, search_results)

        # DEBUG: print what match and score bot is seeing
        print(f"Best match: {best_match}, Score: {score}")

        if score < 70:
            return f"❌ Couldn't find a reliable match for **{movie_title}**. Please check the spelling!"

        # 🎯 NEW: Remove "film" keyword check completely
        # Trust fuzzy score + matching instead

        # Fetch summary of best match
        summary = wikipedia.summary(best_match, sentences=2)
        return f"🎬 **{best_match}**:\n\n{summary}"

    except wikipedia.exceptions.DisambiguationError as e:
        return f"🔎 Multiple results found for **{movie_title}**. Please be more specific!"
    except wikipedia.exceptions.PageError:
        return f"❌ Couldn't find any information for **{movie_title}**."
    except Exception as e:
        return f"⚡ An unexpected error occurred: {e}"

while True:
    try:
        for comment in subreddit.stream.comments(skip_existing=True):
            comment_body = comment.body.lower()

            if bot_username in comment_body:
                try:
                    # Extract the movie name
                    split_text = comment.body.split()
                    mention_index = split_text.index(bot_username)
                    
                    # Everything after the bot mention is assumed to be the movie title
                    movie_title = ' '.join(split_text[mention_index + 1:])

                    if movie_title.strip() == "":
                        reply_text = "🎬 Please provide a movie name after mentioning me!"
                    else:
                        print(f"Searching for movie summary: {movie_title}")
                        reply_text = get_movie_summary(movie_title)

                    comment.reply(reply_text)
                    print(f"Replied to comment by {comment.author.name}")
                    time.sleep(30)  # Sleep to avoid spam
                    
                except Exception as e:
                    print(f"Error replying to comment: {e}")
                    time.sleep(60)

    except Exception as e:
        print(f"Major error: {e}")
        time.sleep(60)