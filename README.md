# 📜 Project Summary: Reddit Movie Summary Bot

## 🛠 Problem Statement:
As a developer from Kerala, I wanted to solve a niche but important problem:
Malayalam movies are often mentioned casually on Reddit, but finding quick summaries for these movies can be difficult, especially when there are multiple movies with similar titles.

## 🚀 Project Goal:
✅ Build a fully autonomous Reddit bot that:

Listens for mentions of my bot name (cocopuffbot) in comments,

Extracts the Malayalam movie name mentioned,

Fetches a short Wikipedia summary intelligently,

Replies automatically within seconds,

Works reliably 24/7 without human intervention.

## 🔥 Key Features:
Fuzzy Matching: Handles minor spelling mistakes in movie names using thefuzz library.

Malayalam Movie Focus: Prioritizes search queries with "Malayalam film" context to improve Wikipedia search accuracy.

Real-Time Listening: Uses Reddit's API (praw) to stream new comments live.

Background Linux Hosting: Bot runs continuously on a home Linux server to avoid cloud hosting costs.

Power Management: System configured to stay awake 24/7 with screen off (energy-efficient setup).

## 🛠 Technical Implementation:
Python 3 for core bot logic.

### Libraries Used:

praw for Reddit API interaction,

wikipedia for movie data fetching,

thefuzz for fuzzy text matching,

python-dotenv for secure secret management.

### Infrastructure:

Deployed on an old Linux laptop configured to stay awake 24/7,

Used nohup to keep the bot alive across sessions,

Configured /etc/systemd/logind.conf to disable lid sleep behavior.

### Security:

Environment variables (.env) used to protect Reddit API credentials,

GitHub .gitignore configured to avoid leaking sensitive files.

## 📈 Challenges Overcome:

Avoiding old comment scraping (only reacting to fresh activity).

Improving Wikipedia search reliability for regional movies.

Managing Linux power and process lifecycle without relying on cloud services.

## 🌟 Outcome:

✅ Built a fully automated Reddit bot from scratch deployed on u/testingground4bots.

✅ Focused on a Malayalam regional use case.

✅ Hosted it completely independently, without needing paid services.

✅ Created a real-world application showcasing automation, APIs, and Linux server management skills.
