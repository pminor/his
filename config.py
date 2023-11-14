import os 

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'ce1b5df5d250e3ajdfjbede09b345c2cd7ee32'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://his:his2023@localhost/his'

class DevConfig(Config):
    DEBUG = True 
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://his:his2023@localhost/his'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


config_options = {
    "development" : DevConfig,
    "production" : ProductionConfig
}
