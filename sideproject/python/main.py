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
from pyintdb.core.utils.field_mapper import IDENTIFIER_KEYS as id_keys
from pyintdb.products.services.brand_service import get_all_brands, get_brand_by_id, create_brand
from pyintdb.products.services.product_service import create_product, get_products, get_product_by_id, get_product_by_name
from pyintdb.products.services.identifier_service import get_or_create_identifier
from pyintdb.products.services.product_service import get_product_by_identifier

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
    loop =1
    continuity =1
    data ={}
    printer("Add properties by writing: Key = value")
    printer("Type 'exit' to quit and 'info' for key values")
    #ADD DATA
    while loop == 1:
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
            print("=]")
            printer("Selected data:")
            for key, value in data.items():
                output = str(key) +" = "+ str(value)
                printer(output)
            print("=]")
            raw_input = input("=] Send it! Yes or no? (Or 'edit') ")
            #PROCESS
            if str.lower(raw_input) == "yes" or str.lower(raw_input) == "y":
                #START FUNCTION
                continuity =0
                loop =0
                #IDENTIFIER SETUP
                identifiers =[] 
                mod_data ={}
                for key, value in data.items():
                    if key.lower() in id_keys:
                        identifiers.append({
                            "type": key.lower(),
                            "value": value
                        })
                    else:
                        mod_data[key] = value
                #CHECK IDENTIFIERS
                if identifiers:
                    results =[]
                    product = create_product(mod_data)
                    product_id = product.get("product_id")

                    for identifier in identifiers:
                        output = get_or_create_identifier(
                        identifier=identifier["value"],
                        type=identifier["type"],
                        product_id=product_id
                    )
                        
                    return results
                else:
                    output = create_product(data)
                    return output
            #EDIT
            elif str.lower(raw_input) == "edit" or str.lower(raw_input) == "e": 
                continuity =1
            #STOP
            else:
                loop =0
                printer("Event cancelled")
        return "Error"
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
            cmd = str.lower(sys.argv[1])
            #
            # BRANDS
            #
            if cmd == "brands" or cmd == "brand":
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
            elif cmd == "products" or cmd == "product":
                #INDEX
                if len(sys.argv) == 2:
                    printer("            *** OPTIONS ***")
                    printer("get id / name / ref")
                    printer("create")
                #MAIN
                else:
                    #CREATE PRODUCT WIZARD
                    if len(sys.argv) == 3:
                        if sys.argv[2] == "create":
                            output = create_product_wiz()
                            printer(output)
                    #GET ALL DATA
                    elif len(sys.argv) == 4:
                        if sys.argv[2] == "get":
                            if sys.argv[3] == "all":
                                for b in get_products():
                                    printer(b)
                    #GET SPECIFIC DATA
                    elif len(sys.argv) == 5:
                        if sys.argv[2] == "get":
                            #BY ID
                            if sys.argv[3] == "id":
                                for key, value in get_product_by_id(sys.argv[4]).items():
                                    output = str(key) +" : "+ str(value)
                                    printer(output)
                            #BY NAME
                            elif sys.argv[3] == "name":
                                output = get_product_by_name(sys.argv[4])
                                product_id = output["id"]
                                if product_id:
                                    for key, value in get_product_by_id(product_id).items():
                                        output = str(key) +" : "+ str(value)
                                        printer(output)
                            #BY REF NO TYPE
                            elif sys.argv[3] == "ref":
                                output = get_product_by_identifier(sys.argv[4])
                                printer(output)
                    elif len(sys.argv) == 6:
                        if sys.argv[2] == "get":
                            #BY REF WITH TYPE
                            if sys.argv[3] == "ref":
                                output = get_product_by_identifier(sys.argv[4],sys.argv[5])
                                printer(output)
    except:
        sys.exit()