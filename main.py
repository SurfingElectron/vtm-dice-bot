import discord
import os
from dotenv.main import load_dotenv

# SEKRITS PRECIOUS
load_dotenv()
TOKEN = os.getenv('TOKEN')

# Set up
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Prints to the console once connection is successful
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Responds to a message with starts with $Hello
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)