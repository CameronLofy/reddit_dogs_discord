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

@client.event
async def on_message(message):
    if message.author == client.user or message.author.bot == True:
        return
    if 'dog' in message.content.lower():
        
        posts = []
        for i in subreddits:
            sub = reddit.subreddit(i)
            for post in sub.hot(limit=15):
                if(post.stickied is False):
                    posts.append(post)
        dog_post = random.choice(posts)
        
        await message.channel.send(dog_post.url)
        await message.channel.send("Post title: " + dog_post.title)
        
        
@client.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(client.user))
    print('------')
        

client.run(TOKEN)