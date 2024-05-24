"""add app entity

Revision ID: 0fc14df78ac3
Revises: fbf94c515e04
Create Date: 2024-05-23 11:23:26.708946

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "0fc14df78ac3"
down_revision: Union[str, None] = "fbf94c515e04"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "app",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("uuid", sa.Unicode(length=255), nullable=False),
        sa.Column("name", sa.Unicode(length=255), nullable=True),
        sa.Column("description", sa.Unicode(length=255), nullable=True),
        sa.Column("secret", sa.LargeBinary(), nullable=False),
        sa.Column("create_date", sa.DateTime(), nullable=False),
        sa.Column("attributes", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("enabled", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name", name="uq_app_name"),
        sa.UniqueConstraint("uuid"),
    )
    op.create_table(
        "app_role",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("uuid", sa.Unicode(length=255), nullable=False),
        sa.Column("role", sa.BigInteger(), nullable=False),
        sa.Column("app", sa.BigInteger(), nullable=False),
        sa.Column("create_date", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["app"], ["app.id"], name="fk_app_role_app", ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["role"], ["role.id"], name="fk_app_role_role", ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("app", "role", name="uq_app_role_app_role"),
        sa.UniqueConstraint("uuid"),
    )

    # ### end Alembic commands ###
    op.execute("ALTER TYPE role_action_resource_type ADD VALUE 'APP';")


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("app_role")
    op.drop_table("app")
    # ### end Alembic commands ###

    # Downgrade the role_action_resource_type type is intentionally ignored because existing records might
    # already depend on it