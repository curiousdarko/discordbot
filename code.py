import discord
import random
from discord_interactions import client
from discord_slash import SlashCommand, SlashContext
from discord_slash.model import ButtonStyle
from discord_slash.utils import manage_components
from discord_slash.utils.manage_commands import create_option, create_choice

intents = discord.Intents.default()
intents.messages = True
intents.components = True

client = discord.Client(intents=intents)
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
    print('Bot is ready.')

@slash.slash(name="fact", description="Get a random fact")
async def get_fact(ctx: SlashContext):
    fact = get_random_fact()
    embed = discord.Embed(title="Random Fact", description=fact, color=discord.Color.blue())
    await ctx.send(embed=embed, components=[create_button()])

@client.event
async def on_component(ctx):
    if ctx.component_id == "get_fact":
        fact = get_random_fact()
        embed = discord.Embed(title="Random Fact", description=fact, color=discord.Color.blue())
        await ctx.edit_origin(embed=embed, components=[create_button()])

def get_random_fact():
    with open('facts.txt', 'r') as file:
        facts = file.readlines()
        fact = random.choice(facts).strip()
    return fact

def create_button():
    return manage_components.create_actionrow(
        manage_components.create_button(
            style=ButtonStyle.PRIMARY,
            label="Get another fact",
            custom_id="get_fact"
        )
    )

client.run('YOUR_BOT_TOKEN')
