#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980002035
#|==============================================================|#

#SETTINGS
from pyintdb.products.repositories.product_repository import lookup_products

def basic_lookup(query: str):
    if not query:
        return {"error": "query is required"}
    
    products = lookup_products(query)

    return {
        "query": query,
        "count": len(products),
        "products": products
    }