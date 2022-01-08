"""add normalized_phone to orders

Revision ID: 57101653ac7d
Revises: d9977bed8c37
Create Date: 2019-06-19 21:16:02.362286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57101653ac7d'
down_revision = 'd9977bed8c37'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'orders',
        sa.Column('normalized_phone', sa.String(100), default=None)
    )


def downgrade():
    op.drop_column('orders', 'normalized_phone')
