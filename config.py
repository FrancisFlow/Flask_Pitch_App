import os

class Config:
    pass



class DevConfig(Config):

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