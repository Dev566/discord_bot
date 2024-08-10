import os

from flask import Flask
from dotenv import load_dotenv , dotenv_values

load_dotenv()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    my_variable = os.getenv('DISCORD_TOKEN', 'default_value')
    print("my_variable "+ my_variable)
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .src import discordBot
    discordBot.run_discord_bot(my_variable)
    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'
    
    # if __name__ == "__main__":
    #     app.run(port=8000, debug=True)

    return app

if __name__ == "__main__":
    app = create_app(None)
    app.run(port=8080)