import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import csv

load_dotenv()

prefix = os.getenv("PREFIX")
token = os.getenv("TOKEN")

client = commands.Bot(command_prefix=prefix, case_insensitive=True)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity = discord.Activity(name='my DMs', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)

    csv_file = csv.reader(open('channels.csv', "rt", encoding="utf-8"), delimiter=",")

    for row in csv_file:
        client.mod_mail_channel = row[0]
        client.resolved_mail_channel = row[1]
        break

client.remove_command("help")


extensions = ['cogs.ModMail']

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)
client.run(token)
