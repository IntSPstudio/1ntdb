#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980002035
#|==============================================================|#

#SETTINGS
from config import DB_PRODUCTS
from pyintdb.core.db_utils import db_cursor
from pyintdb.core.enums.status import Status
from pyintdb.core.repository import fetch_one
from pyintdb.core.utils.field_mapper import validate_update_field
from pyintdb.core.parsing.qty import parse_qty_input
from pyintdb.core.services.unit_service import get_unit_id
from pyintdb.products.services.brand_service import get_or_create_brand

#CREATE PRODUCT WITH NO IDENTIFIER
def create_product(input: dict):
    data = {}
    warnings = []
    #VALIDATE + MAP INPUT
    for key, value in input.items():
        try:
            validated_key = validate_update_field("products", key)
            if validated_key is None:
                warnings.append(f"Skipped field: {key}")
                continue
            data[validated_key] = value
        except ValueError as e:
            warnings.append(str(e))
    #REQUIRED FIELD
    name = data.get("name")
    if not name:
        raise ValueError("name_required")
    products = get_product_by_name(name)
    if products:
        for row in products:
            product_id = row["id"]
            delete_product(product_id)
        #raise ValueError("name_already_exists")
    #BRAND (name -> id)
    brand = data.get("brand_id")
    if brand:
        if brand.isnumeric():
            data["brand_id"] = int(brand)
        else:
            data["brand_id"] = get_or_create_brand(brand)
    #QUANTITY + UNIT RESOLUTION
    raw_qty = data.get("qty_value")
    if raw_qty:
        unit_id = data.get("unit_id")
        qty_value = None
        unit_symbol = None
        if unit_id:
            if unit_id.isnumeric():
                data["qty_value"] = raw_qty
            else:
                data["unit_id"] = get_unit_id(unit_id)
        else:
            qty_value, unit_symbol = parse_qty_input(raw_qty)
            data["qty_value"] = qty_value
            data["unit_id"] = get_unit_id(unit_symbol)
    #INSERT
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
                data.get("brand_id"),
                data.get("category_id"),
                data.get("qty_value"),
                data.get("unit_id"),
                data.get("manufacturer"),
                data.get("made_in"),
                data.get("info"),
                data.get("note"),
            )
        )

        return {
            "product_id": cursor.lastrowid,
            "warnings": warnings
        }
    
#GET PRODUCT WITH IDENTIFIER (EXAMPLE: GTIN)
def get_product_by_identifier(identifier: str, type: str = None):
    #RULES
    if not identifier:
        return {"error": "identifier is required"}
    identifier = identifier.strip()
    #
    try:
        with db_cursor(DB_PRODUCTS) as cursor:

            if type:
                type = type.strip().lower()

                cursor.execute("""
                    SELECT p.*
                    FROM product_identifiers pi
                    JOIN products p ON pi.product_id = p.id
                    WHERE pi.identifier = %s
                      AND pi.type = %s
                      AND p.status_id != 4
                    LIMIT 1
                """, (identifier, type))

            else:
                cursor.execute("""
                    SELECT p.*
                    FROM product_identifiers pi
                    JOIN products p ON pi.product_id = p.id
                    WHERE pi.identifier = %s
                      AND p.status_id != 4
                    LIMIT 1
                """, (identifier,))

            row = fetch_one(cursor)

            if not row:
                return {"found": False}

            return {
                "found": True,
                "product": row
            }
    except Exception as e:
        return {"error": str(e)}

#GET ALL
def get_products():
    with db_cursor(DB_PRODUCTS) as cursor:
        cursor.execute(
            "SELECT * FROM products WHERE status_id = %s",
            (Status.ACTIVE.value,)
        )
        return cursor.fetchall()

#GET ONE BY NAME
def get_product_by_name(name: str) -> dict | None:
    with db_cursor(DB_PRODUCTS) as cursor:
        cursor.execute(
            """
            SELECT id, name, status_id
            FROM products
            WHERE LOWER(name) = %s
            AND status_id = 1
            LIMIT 1
            """,
            (name.lower(),)
        )
        return cursor.fetchone()

#GET ALL BY NAME
def get_products_by_name(name: str) -> list[dict]:
    with db_cursor(DB_PRODUCTS) as cursor:
        cursor.execute(
            """
            SELECT id, name, status_id
            FROM products
            WHERE LOWER(name) = %s
            AND status_id = 1
            """,
            (name.lower(),)
        )
        return cursor.fetchall()

#GET ONE BY ID
def get_product_by_id(product_id: int):
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
            SET status_id = %s
            WHERE id = %s
            """,
            (Status.DELETED.value, product_id)
        )

        return cursor.rowcount > 0