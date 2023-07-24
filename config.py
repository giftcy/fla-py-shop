import os
import pymysql




class Config:
    DEBUG = 0
    SQLALCHEMY_DATABASE_URI = 'pymysql+mysql//'
    SECRET_KEY=os.environ.get('SECRET_KEY')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


class DevelopmentConfig(Config):
    DEBUG = 1
    APP = 'server.py'
    SECRET_KEY=os.environ.get('SECRET_KEY')


class ProductionConfig(Config):
    pass



class TestingConfig(Config):
    pass



config = {
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'testing':TestingConfig,
    'default':DevelopmentConfig
}
