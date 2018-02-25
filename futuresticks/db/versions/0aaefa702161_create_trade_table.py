"""create trade table

Revision ID: 0aaefa702161
Revises:
Create Date: 2018-02-25 16:01:05.103486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0aaefa702161'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'trade',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('code', sa.String(20), nullable=False),
        sa.Column('price', sa.Float),
        sa.Column('description', sa.Unicode(1000)),
        sa.Column('num', sa.Integer),
    )
    pass


def downgrade():
    op.drop_table('trade')
    pass
