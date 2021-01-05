"""review_table

Revision ID: 13884c20b647
Revises: 8cabb52c596a
Create Date: 2021-01-04 14:22:36.152661

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = '13884c20b647'
down_revision = '8cabb52c596a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'review',
        sa.Column('Id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('Title', sa.String(45), nullable=False),
        sa.Column('ReviewText', sa.String(1024), nullable=False),
        sa.Column('Score', sa.Numeric(2, 1), nullable=False),
        sa.Column('DateCreated', sa.Date, nullable=False),
        sa.Column('UserId', sa.Integer, sa.ForeignKey('user.Id'), nullable=False),
        sa.Column('LocationId', sa.Integer, sa.ForeignKey('location.Id'), nullable=False)
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'review' in tables:
        op.drop_table('review')
