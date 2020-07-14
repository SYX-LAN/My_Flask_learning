"""new fields in user model

Revision ID: 164f75abb3d8
Revises: 22e16dd04da0
Create Date: 2020-07-10 13:05:36.654340

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '164f75abb3d8'
down_revision = '22e16dd04da0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
