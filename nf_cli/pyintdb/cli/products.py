#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980001035
#|==============================================================|#

#SETTINGS
from pyintdb.utils.printer import (printer, printer_table)

#MAIN
def handle(args):
    action = args.action
    target = args.target
    if action == "get":
        if target == "all":
            printer("Getting all products")
        else:
            printer(f"Getting product: {target}")
    elif action == "create":
        printer("Creating product")
    else:
        printer("Unknown action")