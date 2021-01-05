"""comment_like_table

Revision ID: 774ce7027729
Revises: 8ef07e3a0358
Create Date: 2021-01-04 14:23:01.356323

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = '774ce7027729'
down_revision = '8ef07e3a0358'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'comment_like',
        sa.Column('UserId', sa.Integer, sa.ForeignKey('user.Id'), primary_key=True, nullable=False),
        sa.Column('CommentId', sa.Integer, sa.ForeignKey('comment.Id'), primary_key=True, nullable=False),
        sa.Column('Liked', sa.Boolean, nullable=False),
        )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'comment_like' in tables:
        op.drop_table('comment_like')
