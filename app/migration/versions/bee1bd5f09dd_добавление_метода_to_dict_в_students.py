"""Добавление метода to_dict в students

Revision ID: bee1bd5f09dd
Revises: b1bb9d2e4db5
Create Date: 2025-03-09 20:46:31.079818

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bee1bd5f09dd'
down_revision: Union[str, None] = 'b1bb9d2e4db5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
