
    
    
from flask import Flask
from flask import request
import threading
import asyncio
import os
from dotenv import load_dotenv , dotenv_values
# from discordBot import discord_bot_run
# from scrapper import process_and_analyse
from botWebsiteChecker import website_summary_bot_run
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return "Thanks for waking me up!"


# @app.route('/scrap', methods=['POST'])
# def scrape_for_location():
#     url = request.json['url']
#     return process_and_analyse(url)

def run_flask():
    port_to_run = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port_to_run)

# def run_discord_bot():
#     new_loop = asyncio.new_event_loop()
#     my_variable = os.getenv('DISCORD_TOKEN', 'default_value')
    
#     asyncio.set_event_loop(new_loop)
#     new_loop.run_until_complete(discord_bot_run(my_variable))
    
def run_website_status():
    new_loop = asyncio.new_event_loop()
    my_variable = os.getenv('DISCORD_TOKEN', 'default_value')
    
    asyncio.set_event_loop(new_loop)
    new_loop.run_until_complete(website_summary_bot_run(my_variable))

if __name__ == '__main__':
    # Run Flask app and Discord bot in separate threads
    flask_thread = threading.Thread(target=run_flask)
    # discord_thread = threading.Thread(target=run_discord_bot)
    web_status_thread = threading.Thread(target=run_website_status)
    
    flask_thread.start()
    # discord_thread.start()
    web_status_thread.start()
    
    flask_thread.join()
    # discord_thread.join()
    web_status_thread.join()
 