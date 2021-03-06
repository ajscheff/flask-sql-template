"""Inadd last name

Revision ID: 9f650c1085a7
Revises: 1698fbcdac93
Create Date: 2020-04-25 17:00:33.570773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f650c1085a7'
down_revision = '1698fbcdac93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('last_name', sa.String(length=128), nullable=True))
    op.execute("UPDATE person SET last_name = 'Smith'")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('person', 'last_name')
    # ### end Alembic commands ###
