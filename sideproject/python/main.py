#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# Version:
# ID: 980002035
#|==============================================================|#

#SETTINGS
import sys
from os import get_terminal_size as cli_size
from pyintdb.services.brand_service import get_all_brands, get_brand_by_id, create_brand
from pyintdb.services.product_service import create_product, get_products, get_product

#CLI PRINTER
def printer(text):
    text = "=] " + str(text)
    try:
        limit = cli_size().columns -1 #SCREEN SIZE
        if len(text) > limit:
            print(text[:limit])
        else:
            print(text)
    except Exception as e:
        print(f"Error printing object: {e}")

#MAIN LOOP
if __name__ == "__main__":
    try:
        #
        # MAIN MENU
        #
        if len(sys.argv) < 2:
            printer("           *** Welcome! Available commands ***")
            printer("products")
            printer("brands")
        else:
            cmd = sys.argv[1]
            #
            # BRANDS
            #
            if cmd == "brands":
                #INDEX
                if len(sys.argv) == 2:
                    printer("            *** OPTIONS ***")
                    printer("get")
                    printer("create")
                #MAIN
                elif len(sys.argv) > 3:
                    #ADD BRAND
                    if sys.argv[2] == "create":
                        if len(sys.argv) > 4:
                            brand = sys.argv[3]
                            info = sys.argv[4]
                            result = create_brand(brand, info)
                        else:
                            result = create_brand(sys.argv[3])
                        
                        printer(result)
                    #GET BRAND
                    elif sys.argv[2] == "get":
                        input = sys.argv[3]
                        if input == "all":
                            for b in get_all_brands():
                                printer(b)
                        else:
                            result = get_brand_by_id(input)
                            printer(result)
            #
            # PRODUCTS
            #
            elif cmd == "products":
                #INDEX
                if len(sys.argv) == 2:
                    printer("            *** OPTIONS ***")
                    printer("get id / ref")
                    printer("create")
                #MAIN
                else:
                    #GET ALL DATA
                    if len(sys.argv) == 4:
                        if sys.argv[2] == "get":
                            if sys.argv[3] == "all":
                                printer("Get all products")
                    #GET SPECIFIC DATA
                    elif len(sys.argv) == 5:
                        if sys.argv[2] == "get":
                            if sys.argv[3] == "id":
                                output = "Get product data from table id: "+ str(sys.argv[4])
                                printer(output)
                            elif sys.argv[3] == "ref":
                                output = "Get product data from by reference code: "+ str(sys.argv[4])
                                printer(output)
    except:
        sys.exit()