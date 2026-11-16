#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980002035
#|==============================================================|#

#SETTINGS
from pyintdb.core.utils.field_mapper import ALLOWED_TABLES
from pyintdb.core.utils.field_mapper import validate_update_field
from pyintdb.core.enums.status import Status
from pyintdb.core.db_utils import db_cursor
from config import DB_PRODUCTS

#GENERIC DB HELPER
def update_field(table: str, user_field: str, value, row_id: int):
    if table not in ALLOWED_TABLES:
        raise ValueError("Invalid table")
    field = validate_update_field(table, user_field)

    query = f"""
    UPDATE {table}
    SET {field} = %s
    WHERE id = %s AND status = %s
    """

    with db_cursor(DB_PRODUCTS) as cursor:
        cursor.execute(query, (value, row_id, Status.ACTIVE.value))
        return cursor.rowcount

#
def fetch_one(cursor):
    row = cursor.fetchone()
    return row if row else None

#PRODUCT LOOKUP
def lookup_products(query: str, limit: int = 20):
    like_query = f"%{query}%"
    active = Status.ACTIVE.value

    with db_cursor(DB_PRODUCTS) as cursor:
        cursor.execute(
            """
            SELECT DISTINCT
                p.id,
                p.name,
                b.name AS brand_name,

                CASE
                    WHEN p.name LIKE %s THEN 'product_name'
                    WHEN b.name LIKE %s THEN 'brand'
                    WHEN i.identifier = %s THEN 'identifier'
                    ELSE 'unknown'
                END AS match_type

            FROM products p

            LEFT JOIN brands b
                ON b.id = p.brand_id
                AND b.status_id = %s

            LEFT JOIN identifiers i
                ON i.product_id = p.id
                AND i.status_id = %s

            WHERE (
                p.name LIKE %s
                OR b.name LIKE %s
                OR i.identifier = %s
            )
            AND p.status_id = %s

            LIMIT %s
            """,
            (
                like_query,
                like_query,
                query,

                active,
                active,

                like_query,
                like_query,
                query,

                active,
                limit
            )
        )

        return cursor.fetchall()