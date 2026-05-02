#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980002035
#|==============================================================|#

#SETTINGS
from pyintdb.core.utils.field_mapper import validate_update_field
from pyintdb.core.enums.status import Status
from pyintdb.core.db_utils import db_cursor
from pyintdb.core.utils.field_mapper import ALLOWED_TABLES

#GENERIC DB HELPER
def update_field(table: str, user_field: str, value, row_id: int):
    if table not in ALLOWED_TABLES:
        raise ValueError("Invalid table")
    field = validate_update_field(table, user_field)

    query = f"""
    UPDATE {table}
    SET {field} = %s
    WHERE id = %s AND status = %s
    """

    with db_cursor() as cursor:
        cursor.execute(query, (value, row_id, Status.ACTIVE.value))
        return cursor.rowcount

#
def fetch_one(cursor):
    row = cursor.fetchone()
    return row if row else None