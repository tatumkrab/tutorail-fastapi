"""add content column to posts table

Revision ID: 6c69d4227af8
Revises: dded09cb1683
Create Date: 2022-11-08 15:15:50.030188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c69d4227af8'
down_revision = 'dded09cb1683'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
