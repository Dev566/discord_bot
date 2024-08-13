# import os

# from flask import Flask
# from dotenv import load_dotenv , dotenv_values

# load_dotenv()

# def create_app(test_config=None):
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)

#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)

#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass

#     # a simple page that says hello
#     @app.route('/')
#     def hello():
#         return 'Hello, World!'
    
#     @app.route('/start')
#     def start_bot():
#         my_variable = os.getenv('DISCORD_TOKEN', 'default_value')
#         from .src import discordBot
#         discordBot.run_discord_bot(my_variable)
#         return 'Started'
    
#     # if __name__ == "__main__":
#     #     app.run(port=8000, debug=True)

#     return app

# if __name__ == '__main__':
#     # Set the port from an environment variable, defaulting to 5000
#     port = int(os.environ.get('PORT', 5000))
#     app = create_app()
#     app.run(port=port)
    
    
from flask import Flask
from flask import request
import threading
import asyncio
import os
from dotenv import load_dotenv , dotenv_values
from discordBot import discord_bot_run
from scrapper import process_and_analyse
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return "Thanks for waking me up!"


@app.route('/scrap', methods=['POST'])
def scrape_for_location():
    url = request.json['url']
    return process_and_analyse(url)

def run_flask():
    port_to_run = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port_to_run)

def run_discord_bot():
    new_loop = asyncio.new_event_loop()
    my_variable = os.getenv('DISCORD_TOKEN', 'default_value')
    
    asyncio.set_event_loop(new_loop)
    new_loop.run_until_complete(discord_bot_run(my_variable))

if __name__ == '__main__':
    # Run Flask app and Discord bot in separate threads
    flask_thread = threading.Thread(target=run_flask)
    discord_thread = threading.Thread(target=run_discord_bot)
    
    flask_thread.start()
    discord_thread.start()
    
    flask_thread.join()
    discord_thread.join()
 