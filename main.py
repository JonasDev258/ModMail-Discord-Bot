import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import csv

load_dotenv()

prefix = os.getenv("PREFIX")
token = os.getenv("TOKEN")

client = commands.Bot(command_prefix=prefix, case_insensitive=True, help_command=None)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity = discord.Activity(name='my DMs', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)

extensions = ['cogs.ModMail']

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)
client.run(token)
