"""Add priority in todo model

Revision ID: f903e548ec9d
Revises: b10765999031
Create Date: 2025-04-10 02:01:10.265754

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f903e548ec9d'
down_revision: Union[str, None] = 'b10765999031'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('priority', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todo', 'priority')
    # ### end Alembic commands ###
