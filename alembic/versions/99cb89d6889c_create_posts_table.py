"""create posts table

Revision ID: 99cb89d6889c
Revises: 
Create Date: 2022-11-22 10:53:53.524519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99cb89d6889c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
