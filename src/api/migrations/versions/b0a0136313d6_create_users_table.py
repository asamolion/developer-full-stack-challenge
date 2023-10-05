"""create users table

Revision ID: b0a0136313d6
Revises: 
Create Date: 2023-10-04 18:50:41.266574

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b0a0136313d6"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("username", sa.String, primary_key=True),
        sa.Column("password", sa.String, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("users")
