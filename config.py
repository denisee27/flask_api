#config.py
import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost:3306/flask_db"

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:''@localhost:3306/flask_db"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:''@localhost:3306/flask_db"

config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}