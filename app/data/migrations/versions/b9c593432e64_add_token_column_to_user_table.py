"""Add Token column to User Table

Revision ID: b9c593432e64
Revises: d46f8a17b349
Create Date: 2021-02-03 15:54:56.834834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9c593432e64'
down_revision = 'd46f8a17b349'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column('Token', sa.String(100)))


def downgrade():
    op.drop_column('user', 'Token')
