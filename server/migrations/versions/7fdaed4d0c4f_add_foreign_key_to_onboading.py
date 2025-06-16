"""add foreign key to onboading

Revision ID: 7fdaed4d0c4f
Revises: 60471d414adf
Create Date: 2025-06-16 12:05:50.845881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7fdaed4d0c4f'
down_revision = '60471d414adf'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            'fk_onboardings_employee_id_employees',
            'employees',
            ['employee_id'],
            ['id']
        )

def downgrade():
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.drop_constraint('fk_onboardings_employee_id_employees', type_='foreignkey')
        batch_op.drop_column('employee_id')