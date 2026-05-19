#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980001035
#|==============================================================|#

#SETTINGS
import argparse
from pyintdb.utils.printer import (printer, printer_table)
from pyintdb.cli import products, timtra

#RULES
ROUTES = {
    "pdb": products.handle,
    "timtra": timtra.handle
}

#START COMMAND LINE
def run_cli():
    #ARGPARSE
    parser = argparse.ArgumentParser(
        prog='1NTDB',
        description='Personal ERP & Inventory System',
        epilog='github.com/IntSPstudio/1ntdb')

    parser.add_argument("module")
    parser.add_argument("action")
    parser.add_argument("target", nargs="?", default=None)
    args = parser.parse_args()
    route_command(args)

#COMMAND ROUTING
def route_command(args):
    module = args.module
    #RULES
    if module not in ROUTES:
        print(f"Unknown module: {module}")
        return
    #SEND
    ROUTES[module](args)