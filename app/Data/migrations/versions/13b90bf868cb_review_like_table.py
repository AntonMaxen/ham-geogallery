"""review_like_table

Revision ID: 13b90bf868cb
Revises: 13884c20b647
Create Date: 2021-01-04 14:22:43.378971

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = '13b90bf868cb'
down_revision = '13884c20b647'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'review_like',
        sa.Column('ReviewId', sa.Integer, sa.ForeignKey('review.Id'), nullable=False),
        sa.Column('UserId', sa.Integer, sa.ForeignKey('user.Id'), nullable=False),
        sa.Column('Liked', sa.Boolean, nullable=False)
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'review_like' in tables:
        op.drop_table('review_like')
