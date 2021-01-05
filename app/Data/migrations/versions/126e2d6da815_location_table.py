"""location_table

Revision ID: 126e2d6da815
Revises: f35a96d885e5
Create Date: 2021-01-04 14:21:51.044626

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = '126e2d6da815'
down_revision = 'f35a96d885e5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'badge',
        sa.Column('Id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('Place', sa.String(45), nullable=False),
        sa.Column('Longitude', sa.DECIMAL(6, 3), nullable=False),
        sa.Column('Latitude', sa.DECIMAL(5, 3), nullable=False),
        sa.Column('Name', sa.String(45), nullable=False),
        sa.Column('UserId', sa.Integer, sa.ForeignKey('user.Id'), nullable=False),
        sa.Column('CategoryId', sa.Integer, sa.ForeignKey('category.Id'), nullable=False)
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'location' in tables:
        op.drop_table('location')
