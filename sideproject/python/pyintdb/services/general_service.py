#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980002035
#|==============================================================|#

#SETTINGS
from utils.field_mapper import validate_update_field
from enums.status import Status
from pyintdb.db_utils import db_cursor
from config import TABLE_DATABASE_MAP

def update_field(table, user_field, value, row_id):
    field = validate_update_field(table, user_field)

    query = f"""
    UPDATE {table}
    SET {field} = %s
    WHERE id = %s AND status = %s
    """

    with db_cursor(TABLE_DATABASE_MAP[table]) as cursor:
        cursor.execute(query, (value, row_id, Status.ACTIVE))
        return cursor.rowcount