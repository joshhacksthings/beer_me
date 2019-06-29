"""empty message

Revision ID: 6cab9a6e1441
Revises: cd17fd1e62ba
Create Date: 2019-06-25 08:18:46.118678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cab9a6e1441'
down_revision = 'cd17fd1e62ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('beer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('beer', sa.String(length=255), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('beer')
    # ### end Alembic commands ###
