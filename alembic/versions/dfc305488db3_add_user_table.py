"""add user table

Revision ID: dfc305488db3
Revises: 2e4571c0f45f
Create Date: 2022-11-22 15:33:27.636467

"""
from doctest import FAIL_FAST
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfc305488db3'
down_revision = '2e4571c0f45f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
