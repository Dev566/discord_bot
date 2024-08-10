# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
from datetime import datetime, timedelta
import time
import requests

# IMPORT THE OS MODULE.
import os

# # IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
# from dotenv import load_dotenv

# # LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
# load_dotenv()

# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = "MTI3MTU1NTUyOTcyNjIzNDYzNg.GZJsuj.MiRqXlsH4ks8uNddR8Mvsj630TsE9R8m6gADdA"


# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client(intents=discord.Intents.default())
time_interval = 60
VIVY_CHANNEL_ID = 1271030253392760916

async def check_website_status(url):
    try:
        response = requests.get(url)
        # Check if the status code indicates success (200 OK)
        if response.status_code == 200:
            return "The website " + url+" is up and running."
        else:
            return "The website  " + url+"  returned status code {response.status_code}."
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


async def send_message_to_channel(chanel_id, message='Hello!'):
    print(f'Logged in as {bot.user.name}')
    channel = bot.get_channel(chanel_id)
    if channel is not None:
        await channel.send(message)  # Send your message here
    else:
        print('Channel not found')

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0
    # for guild in bot.guilds:
    #     print(f'Guild: {guild.name}')
    #     for channel in guild.channels:
    #         print(f'Channel: {channel.name} (ID: {channel.id})')
    for guild in bot.guilds:
    # 	# PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")
        for channel in guild.channels:
            print(f'Channel: {channel.name} (ID: {channel.id})')



	# 	# INCREMENTS THE GUILD COUNTER.
	# 	guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	# print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if message.content == "Testing":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("hey")
		display_message = await check_website_status("https://dev.waku-travel.com/")
		await send_message_to_channel(VIVY_CHANNEL_ID, display_message)

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.



if __name__ == "__main__":  
    bot.run(DISCORD_TOKEN)  