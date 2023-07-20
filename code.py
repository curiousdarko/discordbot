import discord
import random
from discord_slash import SlashCommand, SlashContext

client = discord.Client()
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
    return [
        {
            "type": 1,
            "components": [
                {
                    "type": 2,
                    "label": "Get another fact",
                    "style": 1,
                    "custom_id": "get_fact"
                }
            ]
        }
    ]

client.run('YOUR_DISCORD_TOKEN')
