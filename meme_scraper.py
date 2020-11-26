import praw
import os
from dotenv import load_dotenv


load_dotenv()
CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")

reddit = praw.Reddit(client_id = CLIENT_ID,
                    client_secret = CLIENT_SECRET,
                    user_agent = "meme_bot.script v1 (by u/<Reddit username>)")

allowed_extensions = ['.jpg', '.jpeg', '.png']


def get_meme_url(repetition_handler:"repetition checker", subreddits:"subreddit name" ='memes', lim:"Number of posts to keep in memory" =10)-> "image url":
    
    subreddit = reddit.subreddit(subreddits)
    posts = subreddit.hot()

    loop_counter = 0
    for post in posts:
        img_url = post.url
        _, ext = os.path.splitext(img_url)
        if ext in allowed_extensions:  #making sure that the url received is of an image only
            if loop_counter == repetition_handler:
                return (img_url)    
            loop_counter += 1
        
    else:
        return "error"

if __name__ == "__main__":
    print(get_meme_url(0))