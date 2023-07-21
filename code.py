# youtube.com/@developerlaborotory
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="/", intents=intents) #change the command prefix if u want, for example if you make it ? the command wil now be ?fact instead of /fact

@bot.event
async def on_ready():
    print('We have liftoff!')

@bot.command()
async def fact(ctx):
    fact = get_random_fact()
    embed = discord.Embed(title="Random Fact", description=fact, color=discord.Color.blue())
    await ctx.send(embed=embed)

def get_random_fact():
    with open('facts.txt', 'r') as file:
        facts = file.readlines()
        fact = random.choice(facts).strip()
    return fact

bot.run('YOUR_BOT_TOKEN')
