from datetime import timedelta

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "fmq049kbjmajf734nvadinhfg"
    PERMANENT_SESSION_LIFETIME = timedelta(seconds=30)
    SQLALCHEMY_DATABASE_URI = "sqlite:///user.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True