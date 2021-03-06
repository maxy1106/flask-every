"""empty message

Revision ID: a23a8673ab13
Revises: 86d3ed5bb27b
Create Date: 2020-04-28 14:53:41.496753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a23a8673ab13'
down_revision = '86d3ed5bb27b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cinema_movie',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('c_cinema_id', sa.Integer(), nullable=True),
    sa.Column('c_movie_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['c_cinema_id'], ['cinema_admin_user.id'], ),
    sa.ForeignKeyConstraint(['c_movie_id'], ['movies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cinema_movie')
    # ### end Alembic commands ###
