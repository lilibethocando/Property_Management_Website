"""Added description to payment table

Revision ID: 50426a58eeed
Revises: d00d6959256e
Create Date: 2024-04-22 23:53:57.959971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50426a58eeed'
down_revision = 'd00d6959256e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payment', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
