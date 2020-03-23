import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Config:
    DEBUG = False
    DB_FILE = BASE_DIR.joinpath('application.db').absolute()
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_FILE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = '22d126e0f751479d902e15b69fd99939'
