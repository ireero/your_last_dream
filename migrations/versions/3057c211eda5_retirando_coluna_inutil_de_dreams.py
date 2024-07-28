"""Retirando coluna inutil de Dreams

Revision ID: 3057c211eda5
Revises: dfcc404e2c29
Create Date: 2024-07-26 02:29:39.706161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3057c211eda5'
down_revision = 'dfcc404e2c29'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dreams', schema=None) as batch_op:
        batch_op.drop_column('dream_datetime')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dreams', schema=None) as batch_op:
        batch_op.add_column(sa.Column('dream_datetime', sa.DATETIME(), nullable=False))

    # ### end Alembic commands ###
