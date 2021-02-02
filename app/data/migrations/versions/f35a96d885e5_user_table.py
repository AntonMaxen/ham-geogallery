"""user_table

Revision ID: f35a96d885e5
Revises: bf881b2750c6
Create Date: 2021-01-04 14:21:38.964577

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = 'f35a96d885e5'
down_revision = 'bf881b2750c6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column(
            'Id',
            sa.Integer,
            primary_key=True,
            autoincrement=True),
        sa.Column(
            'FirstName',
            sa.String(45)
        ),
        sa.Column(
            'LastName',
            sa.String(45)
        ),
        sa.Column(
            'Email',
            sa.String(45),
            nullable=False,
            unique=True),
        sa.Column(
            'Username',
            sa.String(45),
            nullable=False,
            unique=True),
        sa.Column(
            'Hash',
            sa.String(255),
            nullable=False),
        sa.Column(
            'Salt',
            sa.String(255),
            nullable=False),
        sa.Column(
            'PhoneNumber',
            sa.String(45),
            unique=True),
        sa.Column(
            'DateOfBirth',
            sa.Date),
        sa.Column(
            'JoinDate',
            sa.Date,
            nullable=False),
        sa.Column(
            'PermissionLevel',
            sa.Integer,
            nullable=False)
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'user' in tables:
        op.drop_table('user')
        print('user')
