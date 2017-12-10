import os


class Config:
    """Main configurations class"""

    NEWS_API_KEY = '47048b08e1bb49c194df8909a510c75d'
    # NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources/{}?apiKey{}'


class ProdConfig(Config):
    """Production configuration class that inherits from the main configurations class"""
    pass


class DevConfig(Config):
    """Configuration class for development stage of the app"""
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
