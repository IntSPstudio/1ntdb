#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# Version:
# ID: 980002035
#|==============================================================|#

#SETTINGS
import sys
from os import get_terminal_size as cli_size
from pyintdb.core.utils.field_mapper import TABLE_FIELDS as table_fields
from pyintdb.products.services.brand_service import get_all_brands, get_brand_by_id, create_brand
from pyintdb.products.services.product_service import create_product, get_products, get_product
from pyintdb.products.services.unit_service import get_unit_id_by_symbol

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

#CREATE PRODUCT WIZARD
def create_product_wiz():
    #START
    continuity =1
    data ={}
    printer("Add properties by writing: Key = value")
    printer("Type 'exit' to quit and 'info' for key values")
    #ADD DATA
    while continuity == 1:
        raw_input = input("=] Add new: ")
        if str.lower(raw_input) == "exit" or str.lower(raw_input) == "quit":
            continuity =0
        elif str.lower(raw_input) == "info" or str.lower(raw_input) == "help":
            a ="=]"
            c =0
            d =""
            for b in table_fields["create_products"]:
                c +=1
                a = a +" "+str(c)+". "+ str(b)
            print(a)
        else:
            parts = raw_input.split("=", 1)
            if len(parts) != 2:
                printer("Invalid format! Use: key = value")
                continue
            key = parts[0].strip()
            value = parts[1].strip()
            data[key] = value
    #SHOW AND CONFIRM DATA
    if data:
        printer("")
        printer("Selected data:")
        for key, value in data.items():
            output = str(key) +" = "+ str(value)
            printer(output)
        printer("")
        raw_input = input("=] Send it! Yes or no? ")
        if str.lower(raw_input) == "yes" or str.lower(raw_input) == "y":
            #START FUNCTION HERE
            output = str(create_product(data))
            #printer(output)
        else:
            printer("Event cancelled")
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
                            output = create_product_wiz()
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