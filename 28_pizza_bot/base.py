from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'pizza.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME') or 'test'
    BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD') or 'test'
    BASIC_AUTH_FORCE = True

    FLASK_ADMIN_SWATCH = 'cerulean'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super secret key'

    BOT_TOKEN = os.environ.get('BOT_TOKEN') or \
        '709202930:AAG0mEFX62ZvYf74JmvZij9yUTLiEwxtq7c'


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
