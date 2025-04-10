"""merge add description and add category migration

Revision ID: eb57c4b33033
Revises: d83f8a7300b3, f5435a488ff2
Create Date: 2025-04-10 03:59:51.675601

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eb57c4b33033'
down_revision: Union[str, None] = ('d83f8a7300b3', 'f5435a488ff2')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
