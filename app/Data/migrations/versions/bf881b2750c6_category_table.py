"""category_table

Revision ID: bf881b2750c6
Revises: 
Create Date: 2021-01-04 14:10:30.856332

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = 'bf881b2750c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'category',
        sa.Column(
            'Id',
            sa.Integer,
            primary_key=True,
            autoincrement=True),
        sa.Column(
            'Name',
            sa.String(45),
            nullable=False),
        sa.Column(
            'ParentId',
            sa.Integer,
            sa.ForeignKey('category.Id', ondelete='CASCADE'),
            nullable=False,
            default=0)
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'category' in tables:
        op.drop_table('category')
        print('category')
