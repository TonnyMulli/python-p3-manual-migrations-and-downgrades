"""Renaming students to scholars

Revision ID: 31d85b859a16
Revises: 791279dd0760
Create Date: 2024-08-02 14:24:22.591298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31d85b859a16'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
