#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980002035
#|==============================================================|#

PRODUCT_MAIN_SCHEMA = {
    "name": {
        "type": "string",
        "required": True,
        "max_length": 255
    },
    "brand_id": {
        "type": "integer",
        "required": False
    },
    "category_id": {
        "type": "integer",
        "required": False
    },
    "qty_value": {
        "type": "decimal",
        "required": False
    },
    "unit_id": {
        "type": "integer",
        "required": False
    }
}