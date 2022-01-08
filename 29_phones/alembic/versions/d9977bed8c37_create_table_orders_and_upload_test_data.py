"""create table orders and upload test data

Revision ID: d9977bed8c37
Revises: 
Create Date: 2019-06-19 18:46:28.409006

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table
import csv
from datetime import datetime


# revision identifiers, used by Alembic.
revision = 'd9977bed8c37'
down_revision = None
branch_labels = None
depends_on = None


def str2datetime(datetime_str):
    try:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S.%f')
    except ValueError:
        return None


def upgrade():
    # create table
    orders_structure = (
        'orders',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('contact_name', sa.String(200)),
        sa.Column('contact_phone', sa.String(100)),
        sa.Column('contact_email', sa.String(150)),
        sa.Column(
            'status',
            sa.Enum('DRAFT', 'FULFILLMENT', 'CANCELED', 'COMPLETED')
        ),
        sa.Column('created', sa.DateTime),
        sa.Column('confirmed', sa.DateTime),
        sa.Column('comment', sa.Text),
        sa.Column('price', sa.Numeric(9, 2))
    )
    op.create_table(*orders_structure)

    # read test data from csv
    orders_cols = ['id', 'contact_name', 'contact_phone', 'contact_email',
                      'status', 'created', 'confirmed', 'comment', 'price']
    orders_data = []
    with open('alembic/versions/test.csv', encoding='utf-8') as csv_fp:
        for orders_row in csv.reader(csv_fp):
            orders_row[5] = str2datetime(orders_row[5])
            orders_row[6] = str2datetime(orders_row[6])
            orders_data.append(dict(zip(orders_cols, orders_row)))

    # insert data
    op.bulk_insert(table(*orders_structure), orders_data)


def downgrade():
    op.drop_table('orders')
