"""Initial

Revision ID: 255694b9f59d
Revises: 
Create Date: 2023-06-03 21:39:49.541667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '255694b9f59d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'users',
        sa.Column('n', sa.INTEGER(), nullable=False),
        sa.Column('id', sa.BIGINT(), nullable=False),
        sa.Column('name', sa.VARCHAR(), nullable=False),
        sa.PrimaryKeyConstraint('n'),
        sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
