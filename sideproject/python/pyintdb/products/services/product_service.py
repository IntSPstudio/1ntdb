#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980002035
#|==============================================================|#

#SETTINGS
from config import DB_PRODUCTS
from pyintdb.core.db_utils import db_cursor
from pyintdb.core.enums.status import Status
from pyintdb.core.utils.field_mapper import validate_update_field
from pyintdb.products.services.brand_service import get_or_create_brand
from pyintdb.products.services.unit_service import get_unit_id_by_symbol

#CREATE PRODUCT WITH NO IDENTIFIER
def create_product(input: dict):
    #NEW DATA
    data = {}
    errors = []
    #CHECK FOR USER ERRORS
    for key, value in input.items():
        try:
            validated_key = validate_update_field("products", key)

            if validated_key is None:
                errors.append(f"Skipped field: {key}")
                continue

            data[validated_key] = value

        except ValueError as e:
            errors.append(str(e))
    #NAME CHECK (SQL NOT NULL)
    name = data.get("name")
    if not name:
        errors.append("error: name_required")
        return errors
    #unit_name = data.get("unit_id")
    #if unit_name:
    #   unit_name = get_unit_id_by_symbol(unit_name)
    #   unit_id = unit_name["id"]
    unit_id = None
    #BRAND CHECK (NAME -> ID)
    brand_name = data.get("brand_name")
    brand_id = None
    if brand_name:
        brand_id = get_or_create_brand(brand_name)
    #COMMIT
    with db_cursor(DB_PRODUCTS) as cursor:
        cursor.execute(
            """
            INSERT INTO products (
                name, brand_id, category_id,
                qty_value, unit_id,
                manufacturer, made_in,
                info, note
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                name,
                brand_id,
                data.get("category_id"),
                data.get("qty_value"),
                unit_id,
                data.get("manufacturer"),
                data.get("made_in"),
                data.get("info"),
                data.get("note"),
            )
        )
        return {"product_id": cursor.lastrowid, "errors": errors}

#GET ALL
def get_products():
    with db_cursor(DB_PRODUCTS) as cursor:
        cursor.execute(
            "SELECT * FROM products WHERE status_id = %s",
            (Status.ACTIVE.value,)
        )
        return cursor.fetchall()

#GET ONE
def get_product(product_id):
    with db_cursor(DB_PRODUCTS) as cursor:
        cursor.execute(
            """
            SELECT * FROM products
            WHERE id = %s AND status_id = %s
            """,
            (product_id, Status.ACTIVE.value)
        )
        return cursor.fetchone()

#UPDATE SELECTED FIELD (NOT READY...)
def update_product(product_id, field, value):
    field = validate_update_field("products", field)

    query = f"""
    UPDATE products
    SET {field} = %s
    WHERE id = %s AND status = %s
    """

    #with db_cursor(DB_PRODUCTS) as cursor:
    #    cursor.execute(query, (value, product_id, Status.ACTIVE))
    #    return cursor.rowcount > 0
#SOFT DELETE VERSION
def delete_product(product_id):
    with db_cursor(DB_PRODUCTS) as cursor:
        cursor.execute(
            """
            UPDATE products
            SET status = %s
            WHERE id = %s
            """,
            (Status.DELETED.value, product_id)
        )

        return cursor.rowcount > 0