import os

class Config:
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    @staticmethod
    def init_app(app):
        pass 




class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'




class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://alex:password@localhost:5432/liberary'
    UPLOADED_PHOTOS_DEST = 'app/static/'


config_options = {
    "dev": DevelopmentConfig,
    "prd": ProductionConfig
}