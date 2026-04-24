#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980002035
#|==============================================================|#

#SETTINGS
from contextlib import contextmanager
from pyintdb.db import get_connection

@contextmanager
def db_cursor():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        yield cursor
        conn.commit()
    finally:
        cursor.close()
        conn.close()