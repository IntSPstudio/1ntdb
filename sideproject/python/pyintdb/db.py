#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980002035
#|==============================================================|#

#SETTINGS
import sys
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASS, DB_NAME

#MASTER CONNECTION
def get_connection():
    try:
        return mysql.connector.connect(
            host= DB_HOST,
            user= DB_USER,
            password= DB_PASS,
            database= DB_NAME
        )
    except mysql.connector.Error as e:
        print("DB ERROR:", e)
        sys.exit(1)