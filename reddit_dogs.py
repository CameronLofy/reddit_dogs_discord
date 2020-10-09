from config import *
import discord
import random
import praw


reddit = praw.Reddit(client_id = reddit_client_id,
                     client_secret = reddit_client_secret,
                     password = reddit_password,
                     user_agent = "Linux device",
                     username = reddit_username)

client = discord.Client()

posted = []

# Funtion to help pick random post without repeating for at least 15 posts
def randomized(posts, posted):
    post = random.choice(posts)
    while post in posted:
        post = random.choice(posts)
    if len(posted) >= 15:
        posted.pop(0)
        posted.append(post)
    else:
        posted.append(post)
    return post
        

@client.event
async def on_message(message):
    if message.author == client.user or message.author.bot == True:
        return
    if 'dog' in message.content.lower():
        print(message.author.id)
        if message.author.id in user_blacklist:
            print("author in blacklist")
            await message.channel.send(f"Shut up {user_blacklist[message.author.id]}")
            return
        posts = []
        for i in subreddits:
            sub = reddit.subreddit(i)
            for post in sub.hot(limit=10):
                if(post.stickied is False):
                    posts.append(post)
        dog_post = randomized(posts, posted)
        print("post sent")
        print(posted)
        await message.channel.send(dog_post.url)
        await message.channel.send("Post title: " + dog_post.title)
        
        
@client.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(client.user))
    print('------')
        

client.run(TOKEN)