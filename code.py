import discord
from discord.ext import commands
import random

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command()
async def fact(ctx):
    fact = get_random_fact()
    embed = discord.Embed(title="Random Fact", description=fact, color=discord.Color.blue())
    await ctx.send(embed=embed)

def get_random_fact():
    with open("facts.txt", "r") as file:
        facts = file.readlines()
    fact = random.choice(facts).strip()
    return fact

bot.run("insert_bot_token") # do not remove the speech marks
