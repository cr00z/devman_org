"""upload initial data

Revision ID: 220267257500
Revises: 4ec217048a1b
Create Date: 2019-06-18 19:58:53.269720

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table
import json


# revision identifiers, used by Alembic.
revision = '220267257500'
down_revision = '4ec217048a1b'
branch_labels = None
depends_on = None


def upgrade():
    items_structure = (
        'items',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('title', sa.String),
        sa.Column('description', sa.Text),
    )
    choices_structure = (
        'choices',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('title', sa.String),
        sa.Column('price', sa.Float),
        sa.Column('item_id', sa.Integer, sa.ForeignKey('items.id'))
    )
    with open('alembic/versions/test_data.json', encoding='utf-8') as test_data_obj:
        test_data = json.load(test_data_obj)
    pizza_items = []
    pizza_choices = []
    for pizza_id, pizza_item in enumerate(test_data, start=1):
        pizza_item['id'] = pizza_id
        pizza_items.append(pizza_item)
        for pizza_choice in pizza_item['choices']:
            pizza_choice['item_id'] = pizza_id
            pizza_choices.append(pizza_choice)
    op.bulk_insert(table(*items_structure), pizza_items)
    op.bulk_insert(table(*choices_structure), pizza_choices)


def downgrade():
    op.execute('DELETE FROM items;')
    op.execute('DELETE FROM choices;')
