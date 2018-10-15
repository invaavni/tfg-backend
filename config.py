"""Configuration file"""

class Config(object):
    """
    Common configurations
    """
    API_URL = '/api/v1.0'


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """
    Production configurations
    """
    DEVELOPMENT = False
    DEBUG = False

APP_CONFIG = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
