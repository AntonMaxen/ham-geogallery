"""badge_table

Revision ID: 9d9a42875d36
Revises: 774ce7027729
Create Date: 2021-01-04 14:23:09.100837

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = '9d9a42875d36'
down_revision = '774ce7027729'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'badge',
        sa.Column(
            'Id',
            sa.Integer,
            primary_key=True,
            autoincrement=True),
        sa.Column(
            'Image',
            sa.BLOB,
            nullable=False),
        sa.Column(
            'Name',
            sa.String(45),
            nullable=False),
        sa.Column(
            'Description',
            sa.String(255))
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'badge' in tables:
        op.drop_table('badge')
        print('badge')
