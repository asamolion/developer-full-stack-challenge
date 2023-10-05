"""create books table

Revision ID: ffa526acf98e
Revises: 4d384e4fc9c7
Create Date: 2023-10-04 18:58:29.432211

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ffa526acf98e"
down_revision: Union[str, None] = "4d384e4fc9c7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "books",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("page_numbers", sa.Integer, nullable=False),
        sa.Column("author_id", sa.Integer),
    )

    op.create_foreign_key("fk_book_author_id", "books", "authors", ["author_id"], ["id"])


def downgrade() -> None:
    op.drop_table("books")
