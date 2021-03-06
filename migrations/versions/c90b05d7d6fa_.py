"""empty message

Revision ID: c90b05d7d6fa
Revises: b33fc1bcc892
Create Date: 2020-04-29 09:27:05.479808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c90b05d7d6fa'
down_revision = 'b33fc1bcc892'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hall_movie',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('h_id', sa.Integer(), nullable=True),
    sa.Column('m_id', sa.Integer(), nullable=True),
    sa.Column('h_m_data', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['h_id'], ['hall.id'], ),
    sa.ForeignKeyConstraint(['m_id'], ['movies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hall_movie')
    # ### end Alembic commands ###
