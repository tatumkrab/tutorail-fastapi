"""add last few columns to posts table

Revision ID: 076e8db3b07e
Revises: bda01b2a8fd8
Create Date: 2022-11-08 16:11:21.054843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '076e8db3b07e'
down_revision = 'bda01b2a8fd8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
