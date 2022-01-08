from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
import os
import datetime


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://login:password@host/db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact_name = db.Column(db.String(200))
    contact_phone = db.Column(db.String(100))
    contact_email = db.Column(db.String(150))
    status = db.Column(Enum('DRAFT', 'FULFILLMENT', 'CANCELED', 'COMPLETED'))
    created = db.Column(db.DateTime)
    confirmed = db.Column(db.DateTime)
    comment = db.Column(db.Text)
    price = db.Column(db.Numeric(9, 2))


def get_order_max_wait_time():
    today = datetime.datetime.utcnow()
    query_func = db.func.min(Orders.created)
    query_filter = Orders.confirmed.is_(None)
    result = db.session.query(query_func).filter(query_filter).one()
    return int((today - result[0]).total_seconds() // 60)


def get_background_color(max_wait_time):
    bgcolor = 'red'
    if max_wait_time <= 30:
        bgcolor = 'yellow'
    if max_wait_time <= 7:
        bgcolor = 'green'
    return bgcolor


def get_orders_wait_count():
    return Orders.query.filter(Orders.confirmed.is_(None)).count()


def get_processed_orders_today_count():
    today_date = datetime.datetime.utcnow().date()
    return Orders.query.filter(Orders.confirmed > today_date).count()


@app.route('/')
def score():
    max_wait_time = get_order_max_wait_time()
    return render_template(
        'score.html',
        bgcolor=get_background_color(max_wait_time),
        max_wait_time=max_wait_time,
        orders_wait=get_orders_wait_count(),
        processed_today=get_processed_orders_today_count()
    )


if __name__ == "__main__":
    app.run()
