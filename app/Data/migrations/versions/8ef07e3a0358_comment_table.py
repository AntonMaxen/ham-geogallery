"""comment_table

Revision ID: 8ef07e3a0358
Revises: 13b90bf868cb
Create Date: 2021-01-04 14:22:51.373652

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.


revision = '8ef07e3a0358'
down_revision = '13b90bf868cb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'comment',
        sa.Column('Id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('CommentText', sa.String(255), nullable=False),
        sa.Column('ReviewId', sa.Integer, sa.ForeignKey('review.Id'), nullable=False),
        sa.Column('UserId', sa.Integer, sa.ForeignKey('user.Id'), nullable=False)
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'comment' in tables:
        op.drop_table('comment')
