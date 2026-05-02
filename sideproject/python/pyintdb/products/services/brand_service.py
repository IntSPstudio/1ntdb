#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980002035
#|==============================================================|#

#SETTINGS
from pyintdb.core.db_utils import db_cursor
from config import DB_PRODUCTS

#ADD
def create_brand(name, info=None):
    with db_cursor(DB_PRODUCTS) as cursor:
        #CHECK IF EXISTS
        cursor.execute(
            "SELECT id FROM brands WHERE name = %s",
            (name,)
        )
        existing = cursor.fetchone()
        if existing:
            return {
                "success": False,
                "id": existing["id"],
                "message": "Brand already exists"
            }
        #ADD NEW ONE
        cursor.execute(
            """
            INSERT INTO brands (name, info)
            VALUES (%s, %s)
            """,
            (name.strip(), info.strip() if info else None)
        )
        return {
            "success": True,
            "id": cursor.lastrowid,
            "message": "Brand created"
        }
#GET OR CREATE
def get_or_create_brand(name):

    with db_cursor(DB_PRODUCTS) as cursor:
        cursor.execute("SELECT id FROM brands WHERE LOWER(name)=%s", (str.lower(name),))
        
        row = cursor.fetchone()
        if row:
            return row["id"]
        cursor.execute(
            "INSERT INTO brands (name) VALUES (%s)",
            (name,)
        )
        return cursor.lastrowid
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