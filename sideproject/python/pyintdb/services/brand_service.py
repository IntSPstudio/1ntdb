#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980002035
#|==============================================================|#

#SETTINGS
from pyintdb.db_utils import db_cursor
from config import DB_PRODUCTS

#ADD
def add_brand(name, info=None):
    with db_cursor(DB_PRODUCTS) as cursor:
        cursor.execute(
            """
            INSERT INTO brands (name, info)
            VALUES (%s, %s)
            """,
            (name.strip(), info.strip() if info else None)
        )
#GET ALL
def get_all_brands():
    with db_cursor(DB_PRODUCTS) as cursor:
        cursor.execute("SELECT * FROM brands")
        return cursor.fetchall()
#GET ONE
def get_brand_by_id(brand_id):
    with db_cursor(DB_PRODUCTS) as cursor:
        cursor.execute(
            "SELECT * FROM brands WHERE id = %s",
            (brand_id,)
        )
        return cursor.fetchone()