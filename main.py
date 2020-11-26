import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from meme_scraper import get_meme_url

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

bot = commands.Bot(command_prefix = '$')


@bot.command(name='binod', help='BINOD!')
async def binod(ctx):
    await ctx.send('binod')


rep_preventor = -1
@bot.command(name='meme', help='Get some fresh memes from your desired subreddit(default = r/memes)\nUsage: $meme <subreddit name>')
async def meme(ctx, subreddit='memes'):
    global rep_preventor
    rep_preventor += 1
    meme_url = get_meme_url(rep_preventor, subreddit)
    if meme_url == 'error':
        await ctx.send("Oops....Could not find a meme. Try again later bwaoy.")
    else:
        await ctx.send(meme_url + '\ntype $help for a list of all commands')

bot.run(TOKEN)
