#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980002035
#|==============================================================|#

#SETTINGS
from config import DB_PRODUCTS
from pyintdb.core.db_utils import db_cursor

#BY SYMBOL
def get_unit_id(value: str) -> int:
    with db_cursor(DB_PRODUCTS) as cursor:
        cursor.execute(
            """
            SELECT id 
            FROM units 
            WHERE (LOWER(symbol) = %s OR LOWER(name) = %s)
            AND status_id = 1 
            LIMIT 1
            """,
            (value.lower(), value.lower())
        )

        result = cursor.fetchone()

        if not result or "id" not in result:
            raise ValueError(f"Unknown unit: {value}")

        return result["id"]