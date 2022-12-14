"""empty message

Revision ID: 3803f794c37e
Revises: 31ba5453b82b
Create Date: 2022-09-01 10:00:19.895765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3803f794c37e'
down_revision = '31ba5453b82b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employers')
    op.add_column('product', sa.Column('price', sa.Float(), nullable=True))
    op.add_column('product', sa.Column('qty', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'qty')
    op.drop_column('product', 'price')
    op.create_table('employers',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('employer_firstname', sa.VARCHAR(length=150), nullable=True),
    sa.Column('employer_lastname', sa.VARCHAR(length=150), nullable=True),
    sa.Column('description', sa.VARCHAR(length=10000), nullable=True),
    sa.Column('date', sa.DATETIME(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
