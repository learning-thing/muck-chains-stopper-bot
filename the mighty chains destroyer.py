# This code was written by https://www.reddit.com/user/Hananelroe
import praw
print(praw.__version__)

Muck_list = ["Muck", "muck", "Muck.", "muck."]

# initialize with appropriate values 
client_id = "CLIENT_ID"
client_secret = "CLIENT_SECRET"
username = "hananelroe"
password = "PASSWORD"
user_agent = "u/hananelroe's comment chains breaker bot"

# creating an authorized reddit instance 
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)

subreddit = reddit.subreddit("DaniDev")
for comment in subreddit.stream.comments(skip_existing=False):
    print(comment.body)
    if comment.body in Muck_list:
        comment.reply("###SHUT\n ^(i am a simple bot that just want to stop muck chains, [here is my source code](https://github.com/hananelroe/muck-chains-stopper-bot))")
