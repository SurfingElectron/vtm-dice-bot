import discord
from discord.ext import commands
import os
from dotenv.main import load_dotenv

from random import randint

# SEKRITS
load_dotenv()
TOKEN = os.getenv('TOKEN')

# Declare Intents
intents = discord.Intents.default()
intents.message_content = True

# Create the bot object
bot = commands.Bot(command_prefix='!', intents=intents)

# Prints to the console once connection is successful
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Rolls dice when user types !roll
@bot.command(
    help = "Rolls a user-specified number of d10s and outputs it as a list.",
    brief = "Rolls a user-specified number of d10s."
)
async def roll(ctx, dice_pool):
    result_list = []

    for _ in range(int(dice_pool)):
        result_list.append(randint(1, 10))
    
    await ctx.channel.send(result_list)

# Run the bot!
bot.run(TOKEN)