#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# VERSION:
# ID: 980002035
#|==============================================================|#

#SETTINGS
import sys
from pyintdb.services.brand_service import get_brands
from pyintdb.services.brand_service import add_brand

def printer(line):
    print("=] ",line)

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
            #Index
            if len(sys.argv) == 2:
                printer("            *** OPTIONS ***")
                printer("all")
                printer("add")
            #All
            elif len(sys.argv) == 3:
                if sys.argv[2] == "all":
                    for b in get_brands():
                        print(b)
            #Add
            elif len(sys.argv) > 3:
                if sys.argv[2] == "add":
                    add_brand(sys.argv[3])
    except:
        sys.exit()