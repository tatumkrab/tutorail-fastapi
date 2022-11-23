import sqlalchemy as sa
from alembic import op
"""add foreign-key to posts table

Revision ID: 02956fb8204f
Revises: dfc305488db3
Create Date: 2022-11-22 15:53:32.444565

"""


# revision identifiers, used by Alembic.
revision = '02956fb8204f'
down_revision = 'dfc305488db3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
