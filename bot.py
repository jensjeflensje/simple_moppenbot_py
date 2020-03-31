import discord
from discord.ext import commands
import random

import config
from req_helper import get_random_joke

bot = commands.Bot(command_prefix=config.prefix)

@bot.event
async def on_ready():
    print(f"{bot.user.name} werkt nu als simple_moppenbot")

@bot.command()
async def mop(ctx):
    try:
        joke = get_random_joke()
    except:
        return await ctx.send("Er ging iets fout :(")
    embed = discord.Embed(title=f"Mop van {joke['author']}", description=joke["joke"])
    embed.set_footer(text=f"{joke['likes']} likes")
    await ctx.send(embed=embed)

bot.run(config.token)