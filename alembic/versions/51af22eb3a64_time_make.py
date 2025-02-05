"""time make

Revision ID: 51af22eb3a64
Revises: 93ffb74d1565
Create Date: 2025-02-01 17:08:13.027276

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '51af22eb3a64'
down_revision: Union[str, None] = '93ffb74d1565'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('reminders', 'time',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.Time(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('reminders', 'time',
               existing_type=sa.Time(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False)
    # ### end Alembic commands ###
