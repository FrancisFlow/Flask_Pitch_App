from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap= Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    #creating application configurations
    app.config.from_object(config_options[config_name])

    #initializing extensions
    bootstrap.init_app(app)

    #Registering Blueprint classes
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app