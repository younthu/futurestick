"""create stop table

Revision ID: 9ab2a54d9005
Revises: 0aaefa702161
Create Date: 2018-02-26 23:35:16.600295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ab2a54d9005'
down_revision = '0aaefa702161'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'stop',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('code', sa.String(20), nullable=False),
        sa.Column('price', sa.Float),
        sa.Column('status', sa.Boolean),
        sa.Column('description', sa.Unicode(1000)),
        sa.Column('num', sa.Integer),
    )
    pass


def downgrade():
    pass
