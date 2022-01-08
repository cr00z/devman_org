"""create items & choices tables

Revision ID: 4ec217048a1b
Revises: 
Create Date: 2019-06-15 16:02:10.789464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ec217048a1b'
down_revision = None
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
    op.create_table(*items_structure)
    op.create_table(*choices_structure)


def downgrade():
    op.drop_table('items')
    op.drop_table('choices')
