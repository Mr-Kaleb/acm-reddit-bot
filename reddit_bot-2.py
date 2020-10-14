import praw
import pdb
import re
import os
reddit = praw.Reddit('bot1',user_agent="bot_test by /u/Reputation_Majestic")

if not os.path.isfile("post_replied_to.txt"):
    posts_replied_to = []

else: 
    with open("posts_replied_to.txt", 'r') as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split('\n')
        posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit('testingground4bots')

for submission in subreddit.hot(limit=10):
    if submission.id not in posts_replied_to:
        if re.search('test', submission.title, re.IGNORECASE):
            submission.reply('hello')
            print(f'Bot replying to: {submission.title}')
            posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", 'w'):
    for post_id in posts_replied_to:
        f.write(post_id + '\n')
