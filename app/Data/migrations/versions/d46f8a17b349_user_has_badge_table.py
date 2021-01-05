"""user_has_badge_table

Revision ID: d46f8a17b349
Revises: 9d9a42875d36
Create Date: 2021-01-04 14:23:33.272211

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = 'd46f8a17b349'
down_revision = '9d9a42875d36'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'badge',
        sa.Column('UserId', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('BadgeId', sa.Integer, primary_key=True, nullable=False),
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'user_has_badge' in tables:
        op.drop_table('user_has_badge')
