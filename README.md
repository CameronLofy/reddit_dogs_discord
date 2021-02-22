# reddit_dogs_discord

This bot sends a random pic of a dog from Reddit anytime a person says 'dog' in their message

### To add this to your channel

Click this link:
https://discord.com/api/oauth2/authorize?client_id=753075390163058688&permissions=55296&scope=bot


### To run this yourself at home ###

- Create a Reddit bot and a Discord bot through the prosepctive websites (Lots of tutorials on that already)
- Keep track of your Reddit bot and Discord bot credentials
- Create a new file in the same directory as your reddit_dogs.py script and call it 'config.py' 
  - In the newly created config.py file copy and paste the code below and replace TOKEN with your Discord bot token.
  - Replace the following reddit variables with your Reddit bot credentials.
- Add or remove any subreddits you would like to be included when getting a random dog picture.

'''
TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

reddit_client_id = "XXXXXXXXXXXXXX"
reddit_client_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"
reddit_username = "XXXXXXXX"
reddit_password = "XXXXXXXXXXXXXXXXXXXX"


subreddits = ("rarepuppers",
              "corgi",
              "puppysmiles",
              "wigglebutts",
              "dogpictures",
              "lookatmydog",
              "DOG",
              "WhatsWrongWithYourDog",
              "dachshund",
              "blop",
              "supermodeldogs",
              "zoomies",
              "dachshunds")
              '''
              
- Add your Discord bot to your server adn run the script. You should see that the bot in the list of members on the right is now online.
- Test it by typing 'dog' anywhere in your message.
