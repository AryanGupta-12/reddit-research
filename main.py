import os
from collections import Counter
from dotenv import load_dotenv
import praw

# Load environment variables
load_dotenv()

# Initialize Reddit API client
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="research-script by u/your_username"
)

SUBREDDITS = ["startups", "Entrepreneur", "MachineLearning"]
POST_LIMIT = 25

KEYWORDS = [
    "ai",
    "machine learning",
    "startup",
    "saas",
    "automation",
    "website",
    "app",
    "api"
]

def analyze_subreddit(name):
    print(f"\nAnalyzing r/{name}...")
    subreddit = reddit.subreddit(name)
    keyword_counter = Counter()

    for post in subreddit.new(limit=POST_LIMIT):
        text = (post.title + " " + (post.selftext or "")).lower()

        for keyword in KEYWORDS:
            if keyword in text:
                keyword_counter[keyword] += 1

    return keyword_counter


def main():
    overall_counter = Counter()

    for subreddit in SUBREDDITS:
        counts = analyze_subreddit(subreddit)
        overall_counter.update(counts)

    print("\nKeyword Frequency Summary:")
    for keyword, count in overall_counter.most_common():
        print(f"{keyword}: {count}")


if __name__ == "__main__":
    main()
