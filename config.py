import os
class Config:
    # simple mail transfer protocol server configurations
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS=True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='Madetowin'
    #PHOTOS DESTINATION

    UPLOADED_PHOTOS_DEST = 'app/static/photos'

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