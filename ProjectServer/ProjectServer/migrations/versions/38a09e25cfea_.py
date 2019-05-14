"""empty message

Revision ID: 38a09e25cfea
Revises: 306265318891
Create Date: 2019-04-22 13:19:53.874921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38a09e25cfea'
down_revision = '306265318891'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reports', sa.Column('photo', sa.LargeBinary(length=4294967295), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reports', 'photo')
    # ### end Alembic commands ###
