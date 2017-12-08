import os


class Config:
    """Main configurations class"""

    NEWS_API_KEY = '739aea22d2814f919546af28438d1048'
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources/{}?apiKey{}'


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
