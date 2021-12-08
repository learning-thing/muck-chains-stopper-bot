# this bot was made by u/hananelroe on reddit
import praw
print(praw.__version__)

Muck_list = ["Muck", "Muck.", "Muck!" 
             "muck", "muck.", "muck!"
             "MUCK", "MUCK.", "MUCK!"]

# initialize with appropriate values
client_id = ""
client_secret = ""
username = "hananelroe"
password = ""
user_agent = "u/hananelroe's comment chains breaker bot"

# creating an authorized reddit instance 
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)

subreddit = reddit.subreddit("DaniDev")
for comment in subreddit.stream.comments(skip_existing=True):
    print(comment.body)
    if comment.body in Muck_list:
        comment.reply("###SHUT\n ^(i am a simple bot that just want to stop muck chains, [here is my source code](https://github.com/hananelroe/muck-chains-stopper-bot))")
