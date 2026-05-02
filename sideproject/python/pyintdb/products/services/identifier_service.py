#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980002035
#|==============================================================|#

#SETTINGS
from config import DB_PRODUCTS
from pyintdb.core.db_utils import db_cursor
from pyintdb.products.repositories.product_repository import fetch_one
from pyintdb.products.services.product_service import get_product_by_name

#GET OR CREATE IDENTIFIER (USER SIDE)
def get_or_create_identifier_dict(data: dict):
    #RULES
    if not isinstance(data, dict):
        return {"error": "input must be a dict"}
    #FETCH
    identifier = data.get("identifier")
    type_ = data.get("type")
    product_id = data.get("product_id")
    product_name = data.get("product_name")
    #FUNC
    return get_or_create_identifier(
        identifier=identifier,
        type=type_,
        product_id=product_id,
        product_name=product_name
    )
#GET OR CREATE IDENTIFIER (EXAMPLE: GTIN)
def get_or_create_identifier(
    identifier: str,
    type: str,
    product_id: int = None,
    product_name: str = None
):
    #RULES
    if not identifier:
        return {"error": "identifier is required"}
    if not product_id and not product_name:
        return {"error": "product_id or product_name is required"}
    if product_id and product_name:
        return {"error": "use either product_id or product_name, not both"}
    #BORING TEXT
    identifier = identifier.replace(" ", "")
    #identifier = identifier.strip()

    type = type.strip().lower()
    #GET PRODUCT ID
    if product_name:
        product = get_product_by_name(product_name)
        product_id = product["id"]
        if not product_id:
            return {"error": f"product '{product_name}' not found"}
    #SEND
    try:
        with db_cursor(DB_PRODUCTS) as cursor:

            #CHECK
            cursor.execute("""
                SELECT id, product_id, identifier, type
                FROM product_identifiers
                WHERE identifier = %s AND type = %s
                LIMIT 1
            """, (identifier, type))

            row = fetch_one(cursor)

            if row:
                return {
                    "id": row["id"],
                    "product_id": row["product_id"],
                    "identifier": row["identifier"],
                    "type": row["type"],
                    "created": False
                }

            #CREATE
            cursor.execute("""
                INSERT INTO product_identifiers (product_id, identifier, type)
                VALUES (%s, %s, %s)
            """, (product_id, identifier, type))

            return {
                "id": cursor.lastrowid,
                "product_id": product_id,
                "identifier": identifier,
                "type": type,
                "created": True
            }

    except Exception as e:
        return {"error": str(e)}