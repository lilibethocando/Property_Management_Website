"""Removed tenant_id from reminders

Revision ID: 111b751d2266
Revises: 913cb1fb999f
Create Date: 2024-04-22 15:08:51.756550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '111b751d2266'
down_revision = '913cb1fb999f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reminder', schema=None) as batch_op:
        batch_op.drop_constraint('reminder_tenant_id_fkey', type_='foreignkey')
        batch_op.drop_column('tenant_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reminder', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tenant_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('reminder_tenant_id_fkey', 'tenant', ['tenant_id'], ['tenant_id'])

    # ### end Alembic commands ###
