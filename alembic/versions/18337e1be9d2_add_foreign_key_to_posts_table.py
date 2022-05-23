"""add foreign key to posts table

Revision ID: 18337e1be9d2
Revises: 1b4faf3695c3
Create Date: 2022-05-23 02:07:34.097402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18337e1be9d2'
down_revision = '1b4faf3695c3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
