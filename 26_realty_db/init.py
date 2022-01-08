from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADVERTS_PER_PAGE = 15
    NEW_BUILD_AGE_LIMIT = 2


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Advertisement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    settlement = db.Column(db.String)
    under_construction = db.Column(db.Boolean)
    description = db.Column(db.Text)
    price = db.Column(db.Integer, index=True)
    oblast_district = db.Column(db.String, index=True)
    living_area = db.Column(db.Float)
    has_balcony = db.Column(db.Boolean)
    address = db.Column(db.String)
    construction_year = db.Column(db.Integer, index=True)
    rooms_number = db.Column(db.SmallInteger)
    premise_area = db.Column(db.Float)
    active = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return '<Advertisement #{}>'.format(self.id)

    def from_dict(self, dictionary):
        for key, value in dictionary.items():
            setattr(self, key, value)
        return self


if __name__ == '__main__':
    app.run()
