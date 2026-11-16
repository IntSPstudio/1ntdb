#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980002035
#|==============================================================|#

#SETTINGS
from api.schemas.products_schema import PRODUCT_MAIN_SCHEMA

#GET MAIN PRODUCT SCHEMA
def get_product_main_schema():
    return {
        "fields": PRODUCT_MAIN_SCHEMA
    }