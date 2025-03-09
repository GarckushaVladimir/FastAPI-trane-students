"""Добавление метода to_dict в students

Revision ID: c9fe5208a4bb
Revises: bee1bd5f09dd
Create Date: 2025-03-09 20:47:44.355845

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9fe5208a4bb'
down_revision: Union[str, None] = 'bee1bd5f09dd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
