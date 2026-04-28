#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980002035
#|==============================================================|#

#SETTINGS
from config import DB_PRODUCTS
from pyintdb.db_utils import db_cursor

#BY SYMBOL 
def get_unit_id_by_symbol(symbol: str) -> int | None:
    with db_cursor(DB_PRODUCTS) as cursor:
        cursor.execute(
            "SELECT id FROM units WHERE symbol = %s AND status_id = 1 LIMIT 1",
            (symbol,)
        )
        result = cursor.fetchone()
        if result:
            return result
        return None