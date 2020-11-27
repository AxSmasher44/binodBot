# BinodBot
binodBot is a discord bot that scrapes memes from your subreddit of choice and sends them on a discord server's text channel.




### Instructions:

1. Create a discord bot application from the discord developer portal and give it the following permissions:

    - Text Permissions
  
    - Send Messages
  
    - embed links
  
    - attach files



2. Create a reddit application

3. Create a .env file in the same folder as the script and put the following stuff in it:

```
  # .env

  DISCORD_TOKEN=<your discord app token>  
  
  DISCORD_GUILD=<your discord server name>  
  
  REDDIT_CLIENT_ID=<your reddit app client ID>  
  
  REDDIT_CLIENT_SECRET=<your reddit app client secret>
```

4. Run `main.py` to activate the bot!
