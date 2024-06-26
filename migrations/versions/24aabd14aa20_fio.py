"""-FIO

Revision ID: 24aabd14aa20
Revises: 3d33b32902bc
Create Date: 2024-06-24 18:07:13.518846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24aabd14aa20'
down_revision = '3d33b32902bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('accept', schema=None) as batch_op:
        batch_op.drop_column('patronymic')
        batch_op.drop_column('last_name')
        batch_op.drop_column('first_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('accept', schema=None) as batch_op:
        batch_op.add_column(sa.Column('first_name', sa.VARCHAR(length=20), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('last_name', sa.VARCHAR(length=20), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('patronymic', sa.VARCHAR(length=20), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
