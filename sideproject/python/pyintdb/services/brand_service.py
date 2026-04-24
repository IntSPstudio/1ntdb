#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980002035
#|==============================================================|#

#SETTINGS
from pyintdb.db_utils import db_cursor

#ADD
def add_brand(name):
    with db_cursor() as cursor:
        cursor.execute(
            "INSERT INTO brands (name) VALUES (%s)",
            (name,)
        )

#GET ALL
def get_brands():
    with db_cursor() as cursor:
        cursor.execute("SELECT * FROM brands")
        results = cursor.fetchall()
        return results