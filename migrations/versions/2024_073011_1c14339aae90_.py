"""empty message

Revision ID: 1c14339aae90
Revises: 56d08955fcab
Create Date: 2024-07-30 11:46:32.460221

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c14339aae90'
down_revision = '56d08955fcab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mailbox_activation',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=False),
    sa.Column('updated_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
    sa.Column('mailbox_id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=32), nullable=False),
    sa.Column('tries', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['mailbox_id'], ['mailbox.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_mailbox_activation_code'), 'mailbox_activation', ['code'], unique=False)
    op.create_index(op.f('ix_mailbox_activation_mailbox_id'), 'mailbox_activation', ['mailbox_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_mailbox_activation_mailbox_id'), table_name='mailbox_activation')
    op.drop_index(op.f('ix_mailbox_activation_code'), table_name='mailbox_activation')
    op.drop_table('mailbox_activation')
    # ### end Alembic commands ###
