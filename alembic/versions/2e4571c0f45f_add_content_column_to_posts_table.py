"""add content column to posts table

Revision ID: 2e4571c0f45f
Revises: 99cb89d6889c
Create Date: 2022-11-22 15:22:58.866018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e4571c0f45f'
down_revision = '99cb89d6889c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
