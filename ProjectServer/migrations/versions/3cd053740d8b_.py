"""empty message

Revision ID: 3cd053740d8b
Revises: a0b64816947e
Create Date: 2019-03-26 21:03:20.406593

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3cd053740d8b'
down_revision = 'a0b64816947e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'user_email',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_general_ci', length=24),
               nullable=False)
    op.alter_column('users', 'user_name',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_general_ci', length=24),
               nullable=False)
    op.alter_column('users', 'user_phone',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=12),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'user_phone',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=12),
               nullable=True)
    op.alter_column('users', 'user_name',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_general_ci', length=24),
               nullable=True)
    op.alter_column('users', 'user_email',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_general_ci', length=24),
               nullable=True)
    # ### end Alembic commands ###