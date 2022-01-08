# Here will be catalog models for SQLAlchemy
from base import db


class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    choices = db.relationship("Choices")


class Choices(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    price = db.Column(db.Float)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    item = db.relationship(Items, backref='Items')
