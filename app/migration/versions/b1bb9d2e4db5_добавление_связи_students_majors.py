"""Добавление связи students-majors

Revision ID: b1bb9d2e4db5
Revises: 736dd469a513
Create Date: 2025-03-09 19:12:06.987798

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b1bb9d2e4db5'
down_revision: Union[str, None] = '736dd469a513'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
