#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980002035
#|==============================================================|#

#CHECK IF TABLE FIELD EXISTS
def field_check(input):
    input = str("").join(i for i in input.lower() if i.isalnum())
    field_alias = {
        "status": "status_id",
        "parent": "parent_id",
        "man": "manufacturer",

        "qty": "qty_value",
        "cat": "category_id"
    }
    allowed_fields = {
        "id", "code", "name", "type", "info", "note", "identifier",
        "manufacturer", "made_in", "extra",

        "brand_id", "category_id", "status_id", "unit_id"
        "created_at", "updated_at"
    }
    field = field_alias.get(input, input)

    if field in allowed_fields:
        return field
    return None