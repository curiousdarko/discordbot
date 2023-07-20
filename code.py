import discord
import random
from discord_components import DiscordComponents, Button, ButtonStyle

client = discord.Client()
DiscordComponents(client)

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!fact'):
        fact = get_random_fact()
        embed = discord.Embed(title="Random Fact", description=fact, color=discord.Color.blue())
        await message.channel.send(embed=embed, components=[Button(style=ButtonStyle.blue, label="Get another fact", custom_id="get_fact")])

@client.event
async def on_button_click(interaction):
    if interaction.custom_id == "get_fact":
        fact = get_random_fact()
        embed = discord.Embed(title="Random Fact", description=fact, color=discord.Color.blue())
        await interaction.message.edit(embed=embed)

def get_random_fact():
    with open('facts.txt', 'r') as file:
        facts = file.readlines()
        fact = random.choice(facts).strip()
    return fact

client.run('YOUR_DISCORD_TOKEN')
