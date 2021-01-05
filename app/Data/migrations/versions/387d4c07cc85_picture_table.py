"""picture_table

Revision ID: 387d4c07cc85
Revises: a152efd05762
Create Date: 2021-01-04 14:22:22.942564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy.engine.reflection import Inspector

revision = '387d4c07cc85'
down_revision = 'a152efd05762'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'picture',
        sa.Column('Id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('ImageName', sa.String(45), nullable=False),
        sa.Column('Date', sa.Date, nullable=False),
        sa.Column('UserId', sa.Integer, sa.ForeignKey('user.Id'), nullable=False),
        sa.Column('LocationId', sa.Integer, sa.ForeignKey('location.Id'), nullable=False),
        sa.Column('FileName', sa.String(45), nullable=False)
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'picture' in tables:
        op.drop_table('picture')
