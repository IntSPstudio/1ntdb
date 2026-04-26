#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# VERSION:
# ID: 980002035
#|==============================================================|#

#SETTINGS
import sys
from os import get_terminal_size as cli_size
from pyintdb.services.brand_service import get_all_brands
from pyintdb.services.brand_service import get_brand_by_id
from pyintdb.services.brand_service import add_brand

#CLI PRINTER
def printer(text):
    text = "=] " + str(text)
    try:
        limit = cli_size().columns #SCREEN SIZE
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
            printer("brands")
        cmd = sys.argv[1]
        #
        # BRAND
        #
        if cmd == "brands":
            #INDEX
            if len(sys.argv) == 2:
                printer("            *** OPTIONS ***")
                printer("get")
                printer("add")
            #MAIN
            elif len(sys.argv) > 3:
                #Add
                if sys.argv[2] == "add":
                    if len(sys.argv) > 4:
                        brand = sys.argv[3]
                        info = sys.argv[4]
                        result = add_brand(brand, info)
                    else:
                        result = add_brand(sys.argv[3])
                #Get
                if sys.argv[2] == "get":
                    input = sys.argv[3]
                    if input == "all":
                        for b in get_all_brands():
                            printer(b)
                    else:
                        result = get_brand_by_id(input)
                        printer(result)
    except:
        sys.exit()