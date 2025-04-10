"""category field added in todo models from main

Revision ID: 1cc7e3052c33
Revises: f5435a488ff2
Create Date: 2025-04-10 12:27:06.254126

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '1cc7e3052c33'
down_revision: Union[str, None] = 'f5435a488ff2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('category', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todo', 'category')
    # ### end Alembic commands ###
