"""visited_location_table

Revision ID: a152efd05762
Revises: 7a8e0c562f20
Create Date: 2021-01-04 14:22:12.103194

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.


revision = 'a152efd05762'
down_revision = '7a8e0c562f20'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'visited_location',
        sa.Column(
            'LocationId',
            sa.Integer,
            sa.ForeignKey('location.Id', ondelete='CASCADE'),
            primary_key=True,
            nullable=False),
        sa.Column(
            'UserId',
            sa.Integer,
            sa.ForeignKey('user.Id', ondelete='CASCADE'),
            primary_key=True,
            nullable=False)
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'visited_location' in tables:
        op.drop_table('visited_location')
        print('visited_location')
