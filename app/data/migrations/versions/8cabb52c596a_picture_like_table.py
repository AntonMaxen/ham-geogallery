"""picture_like_table

Revision ID: 8cabb52c596a
Revises: 387d4c07cc85
Create Date: 2021-01-04 14:22:27.553965

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
from sqlalchemy.engine.reflection import Inspector

revision = '8cabb52c596a'
down_revision = '387d4c07cc85'
branch_labels = None
depends_on = None


# revision identifiers, used by Alembic.

def upgrade():
    op.create_table(
        'picture_like',
        sa.Column(
            'PictureId',
            sa.Integer,
            sa.ForeignKey('picture.Id', ondelete='CASCADE'),
            primary_key=True,
            nullable=False),
        sa.Column(
            'UserId',
            sa.Integer,
            sa.ForeignKey('user.Id', ondelete='CASCADE'),
            primary_key=True,
            nullable=False),
        sa.Column(
            'Liked',
            sa.Boolean,
            nullable=False)
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'picture_like' in tables:
        op.drop_table('picture_like')
        print('picture_like')
