"""add content column

Revision ID: 02ef6b5fa989
Revises: b7c4d19fe0be
Create Date: 2022-05-23 01:56:57.394977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02ef6b5fa989'
down_revision = 'b7c4d19fe0be'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
