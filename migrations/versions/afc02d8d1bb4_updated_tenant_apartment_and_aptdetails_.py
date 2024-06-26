"""Updated Tenant, Apartment and aptDetails tables

Revision ID: afc02d8d1bb4
Revises: 50426a58eeed
Create Date: 2024-04-23 12:19:13.693741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afc02d8d1bb4'
down_revision = '50426a58eeed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('apartment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('apartment_details_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('apartment_tenant_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'apartment_details', ['apartment_details_id'], ['apartment_details_id'])
        batch_op.drop_column('tenant_id')

    with op.batch_alter_table('apartment_details', schema=None) as batch_op:
        batch_op.drop_constraint('apartment_details_apartment_id_fkey', type_='foreignkey')
        batch_op.drop_column('apartment_id')

    with op.batch_alter_table('tenant', schema=None) as batch_op:
        batch_op.add_column(sa.Column('apartment_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'apartment', ['apartment_id'], ['apartment_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tenant', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('apartment_id')

    with op.batch_alter_table('apartment_details', schema=None) as batch_op:
        batch_op.add_column(sa.Column('apartment_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('apartment_details_apartment_id_fkey', 'apartment', ['apartment_id'], ['apartment_id'])

    with op.batch_alter_table('apartment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tenant_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('apartment_tenant_id_fkey', 'tenant', ['tenant_id'], ['tenant_id'])
        batch_op.drop_column('apartment_details_id')

    # ### end Alembic commands ###
