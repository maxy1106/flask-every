"""empty message

Revision ID: e1c0802f31d1
Revises: 73578fda2e55
Create Date: 2020-04-27 15:02:14.607321

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e1c0802f31d1'
down_revision = '73578fda2e55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cinema_admin_user', sa.Column('is_verify', sa.Boolean(), nullable=True))
    op.drop_column('cinema_admin_user', 'id_verify')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cinema_admin_user', sa.Column('id_verify', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.drop_column('cinema_admin_user', 'is_verify')
    # ### end Alembic commands ###
