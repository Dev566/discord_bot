# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
from datetime import datetime, timedelta
import time
import requests
import asyncio

# IMPORT THE OS MODULE.
import os

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
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
        return f'The website **{url}** is down!'


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
    await send_message_to_channel(VIVY_CHANNEL_ID, "I will in testing phase. Testing 3 min status update.")
    while not bot.is_closed():
        print("Checking status")
        status_message = await check_website_status("https://dev.waku-travel.com/")
        print("Checked status")
        await send_message_to_channel(VIVY_CHANNEL_ID,status_message)
        print("Message send")
        # Wait for 3 hours (10800 seconds) before checking again
        await asyncio.sleep(10800/60)  # Sleep for 3 hours   


async def check_website_status_loop():
    await bot.wait_until_ready()
    

    while not bot.is_closed():
        status_message = check_website_status("https://dev.waku-travel.com/")

        await send_message_to_channel(VIVY_CHANNEL_ID,status_message)
        
        # Wait for 3 hours (10800 seconds) before checking again
        await asyncio.sleep(10800)  # Sleep for 3 hours        

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.

def website_summary_bot_run(discord_bot_key):
    # bot.loop.create_task(check_website_status_loop())
    # check_website_status_loop()
    bot.run(discord_bot_key)
