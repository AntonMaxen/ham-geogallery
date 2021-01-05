"""rating_table

Revision ID: 7a8e0c562f20
Revises: 126e2d6da815
Create Date: 2021-01-04 14:21:59.487061

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = '7a8e0c562f20'
down_revision = '126e2d6da815'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'rating',
        sa.Column('UserId', sa.Integer, sa.ForeignKey('user.Id'), nullable=False),
        sa.Column('LocationId', sa.Integer, sa.ForeignKey('location.Id'),  nullable=False),
        sa.Column('Score', sa.Numeric(2, 1), nullable=False)
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'rating' in tables:
        op.drop_table('rating')
