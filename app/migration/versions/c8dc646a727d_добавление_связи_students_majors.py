"""Добавление связи students-majors

Revision ID: c8dc646a727d
Revises: c9fe5208a4bb
Create Date: 2025-03-09 21:17:22.223633

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c8dc646a727d'
down_revision: Union[str, None] = 'c9fe5208a4bb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
