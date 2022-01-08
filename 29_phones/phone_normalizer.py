import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
import phonenumbers as ph


def normalize_phone_number(phone_str):
    phone_number = ph.parse(phone_str, 'RU')
    # imho "is_possible_number" more correct than "is_valid_number" because
    # phone code database may be outdated
    if ph.is_possible_number(phone_number):
        return ph.format_number(phone_number, ph.PhoneNumberFormat.INTERNATIONAL)
    else:
        return "Impossible number"


Base = declarative_base()


class Orders(Base):
    __tablename__ = 'orders'
    id = sa.Column(sa.Integer, primary_key=True)
    contact_name = sa.Column(sa.String(200))
    contact_phone = sa.Column(sa.String(100))
    contact_email = sa.Column(sa.String(150))
    status = sa.Column(sa.Enum('DRAFT', 'FULFILLMENT', 'CANCELED', 'COMPLETED'))
    created = sa.Column(sa.DateTime)
    confirmed = sa.Column(sa.DateTime)
    comment = sa.Column(sa.Text)
    price = sa.Column(sa.Numeric(9, 2))
    normalized_phone = sa.Column(sa.String(100))


engine = sa.create_engine('sqlite:///orders1.db', echo=True)
session = sa.orm.sessionmaker(bind=engine)()

while True:
    for order in session.query(Orders).filter(Orders.normalized_phone.is_(None)):
        order.normalized_phone = normalize_phone_number(order.contact_phone)
    session.commit()
