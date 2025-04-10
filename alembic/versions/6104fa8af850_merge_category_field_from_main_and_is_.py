"""merge category field from main and is_deleted field from dev

Revision ID: 6104fa8af850
Revises: 1cc7e3052c33, ca6618db2b36
Create Date: 2025-04-10 12:41:40.556823

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6104fa8af850'
down_revision: Union[str, None] = ('1cc7e3052c33', 'ca6618db2b36')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
