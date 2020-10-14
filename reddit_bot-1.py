import praw

reddit = praw.Reddit('bot1', user_agent="bot_test by /u/Reputation_Majestic")



subreddit = reddit.subreddit("testingground4bots")

for submission in subreddit.hot(limit=5):
    print(f"Title: {submission.title}")
