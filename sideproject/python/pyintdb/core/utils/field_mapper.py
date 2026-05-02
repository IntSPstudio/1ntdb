#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980002035
#|==============================================================|#

#ALLOWED TABLES
ALLOWED_TABLES = {
    "products",
    "brands",
    "units",
    "categories",
    "product_identifiers",
    "product_prices"
}

#SHORTCUT
FIELD_ALIAS = {
    "basic": {
        "man": "manufacturer",
        "qty": "qty_value",
        "create": "created_at",
        "update": "updated_at",
        "status": "status_id",
        "brand": "brand_id",
        "cat": "category_id",
        "parent": "parent_id",
        "unit": "unit_id"
    }
}
#WHITE LIST BY TABLE NAMES
TABLE_FIELDS = {
    "create_products": {
        "brand", "brand_id","category", "category_id", "unit", "unit_id",
        "name", "type", "info", "note", "qty_value", "made_in",
        "manufacturer", "gtin", "gtin_value"
    },
    "brands": {
        "id", "name", "info", "status_id", "brand_id",
        "created_at", "updated_at"
    },
    "products": {
        "id", "status_id", "brand_id", "category_id",  "unit_id",
        "name", "type", "info", "note", "qty_value", "made_in",
        "manufacturer", "created_at", "updated_at", "brand_name"
    },
    "units": {
        "id", "status_id", "name", "symbol", "created_at", "updated_at"
    }
}

#READ ONLY FIELDS
READ_ONLY_FIELDS = {
    "id",
    "created_at",
    "updated_at"
}

IDENTIFIER_KEYS = {
    "ean13",
    "ean8",
    "ean",
    "upc",
    "barcode",
    "sku",
    "isbn"
}

#BORING TEXT
def _clean_input(user_input: str) -> str:
    #Only: a-z, 0-9 ja _
    return "".join(
        c for c in user_input.lower()
        if c.isalnum() or c == "_"
    )

#CHANGE USER INPUT OR MAKE ERROR
def validate_field(table: str, user_input: str) -> str:
    #BORING TEXT
    cleaned = _clean_input(user_input)
    #SHORTCUT
    field = FIELD_ALIAS["basic"].get(cleaned, cleaned)
    #TABLE NAME CHECK
    if table not in TABLE_FIELDS:
        raise ValueError(f"Invalid table: {table}")
    #CHECK TABLE FIELD
    if field not in TABLE_FIELDS[table]:
        raise ValueError(f"Invalid field '{field}' for table '{table}'")
    return field

#CHANGE USER INPUT OR MAKE ERROR WITH READ ONLY TABLES
def validate_update_field(table: str, user_input: str) -> str:
    field = validate_field(table, user_input)

    if field in READ_ONLY_FIELDS:
        raise ValueError(f"Field '{field}' is read-only")

    return field