"""empty message

Revision ID: f4052f6cc66a
Revises: f5d6101f885c
Create Date: 2019-05-06 20:43:20.055204

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f4052f6cc66a'
down_revision = 'f5d6101f885c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employees', sa.Column('employ_photo', sa.LargeBinary(length=4294967295), nullable=True))
    op.alter_column('employees', 'empliye_password',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=100),
               nullable=True)
    op.add_column('users', sa.Column('user_photo', sa.LargeBinary(length=4294967295), nullable=True))
    op.alter_column('users', 'user_password',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=100),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'user_password',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=100),
               nullable=False)
    op.drop_column('users', 'user_photo')
    op.alter_column('employees', 'empliye_password',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=100),
               nullable=False)
    op.drop_column('employees', 'employ_photo')
    # ### end Alembic commands ###