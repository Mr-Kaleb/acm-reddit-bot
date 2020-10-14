import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("testingground4bots")

for submission in subreddit.hot(limit=5):
    print(f"Title: {submission.title}")
