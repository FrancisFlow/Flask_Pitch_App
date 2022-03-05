import os

class Config:

    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='Madetowin'

class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://francis:Master@localhost/pitchworld'


    Debug = True

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass


#configuration options
config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test':TestConfig
}