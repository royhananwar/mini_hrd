'''Config File'''

class Config(object):
    '''
    Basic Configuration
    '''


class DevelopmentConfig(Config):
    '''
    Development Config
    '''

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    '''
    Production Config
    '''
    
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
