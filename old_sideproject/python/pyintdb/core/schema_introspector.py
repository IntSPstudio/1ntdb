#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980002035
#|==============================================================|#

#SETTINGS
from pyintdb.core.db_utils import db_cursor
from pyintdb.core.utils.field_mapper import ALLOWED_TABLES

#GENERATE TABLE SCHEMA
def get_table_schema(table_name: str):
    if table_name not in ALLOWED_TABLES:
        raise ValueError("Invalid table")

    query = """
        SELECT 
            COLUMN_NAME,
            DATA_TYPE,
            IS_NULLABLE,
            COLUMN_DEFAULT,
            CHARACTER_MAXIMUM_LENGTH
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = %s
    """

    with db_cursor() as cursor:
        cursor.execute(query, (table_name,))
        columns = cursor.fetchall()

    schema = {}

    for col in columns:
        name = col["COLUMN_NAME"]

        schema[name] = {
            "type": map_db_type(col["DATA_TYPE"]),
            "required": col["IS_NULLABLE"] == "NO" and col["COLUMN_DEFAULT"] is None,
            "max_length": col["CHARACTER_MAXIMUM_LENGTH"],
            "default": col["COLUMN_DEFAULT"]
        }

    return schema

#HELPER
def map_db_type(db_type: str) -> str:
    mapping = {
        "int": "integer",
        "varchar": "string",
        "text": "string",
        "decimal": "decimal",
        "datetime": "datetime"
    }

    return mapping.get(db_type, "string")