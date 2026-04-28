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
from pyintdb.services.product_service import get_products, get_product

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
                            for key, value in get_brand_by_id(input).items():
                                output = str(key) +" : "+ str(value)
                                printer(output)
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
                    #CREATE PRODUCT WIZARD
                    if len(sys.argv) == 3:
                        if sys.argv[2] == "create":
                            printer("Create product!")
                    #GET ALL DATA
                    elif len(sys.argv) == 4:
                        if sys.argv[2] == "get":
                            if sys.argv[3] == "all":
                                for b in get_products():
                                    printer(b)
                    #GET SPECIFIC DATA
                    elif len(sys.argv) == 5:
                        if sys.argv[2] == "get":
                            if sys.argv[3] == "id":
                                for key, value in get_product(sys.argv[4]).items():
                                    output = str(key) +" : "+ str(value)
                                    printer(output)
                            elif sys.argv[3] == "ref":
                                output = "Get product data from by reference code: "+ str(sys.argv[4])
                                printer(output)
    except:
        sys.exit()