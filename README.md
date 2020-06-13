# A Discord Bot for Handling Mod Mail

An example of a bot that can be used for mod mail written in Python. This can be setup by users who have very little knowledge of bots, and requires no DB to setup. This bot has been designed to run without a db for simplicity. It uses a CSV file and .env file to store the small amount of data it requires to function. Or it can be used an example.

### Running
1. Make sure to have Python 3.5 or higher installed on your machine.
2. Install the Discord.py library
3. Install python-dotenv

If you are on Windows: ``py -3 -m pip install -U discord.py``

From PyPI: ``python3 -m pip install -U discord.py``

Run the code by running the `main.py` through python. The bot will then run until it is quit.

### Setting Up
Make sure to have a bot account first. You will need your token from the developer menu which you can paste in the `.env` file. https://discordpy.readthedocs.io/en/latest/discord.html#discord-intro

You can run the `!help` command from withing discord once the bot is running for further instructions.

The bot contains a setup command `!setup <incoming mail channel> <resolved mail channel>`
This command takes 2 arguments. You need to create 2 channels, and pass it the ID value of the channel.

To get the ID value you need to enable developer mode through discord: https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-

These values will be stored in the `channels.csv` file. Alternatively you can open this file, and manually
add the channel_id values to its first line, seperated by a comma. Ex. `12345677894544646,5463874758745874`

The default command prefix is `!` which can be changed by editing the values in the `.env` file.

### Requirements
Python 3.5.3+
python-dotenv 0.13.0 
