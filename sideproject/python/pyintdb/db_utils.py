#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980002035
#|==============================================================|#

#SETTINGS
from contextlib import contextmanager
from pyintdb.db import get_connection

#MAIN
@contextmanager
def db_cursor(db_name):
    conn = get_connection(db_name)
    cursor = conn.cursor(dictionary=True)
    try:
        yield cursor
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()