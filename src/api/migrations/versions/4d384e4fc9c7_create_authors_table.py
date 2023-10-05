"""create authors table

Revision ID: 4d384e4fc9c7
Revises: b0a0136313d6
Create Date: 2023-10-04 18:53:37.014419

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4d384e4fc9c7"
down_revision: Union[str, None] = "b0a0136313d6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "authors",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("authors")
