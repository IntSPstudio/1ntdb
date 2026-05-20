#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980001035
#|==============================================================|#

#SETTINGS
from pyintdb.cli.router import run_cli

"""
    PDB = Product database
    AST = Inventory / stock
    TMS = Timtra (Time management system)
    FLT = Fleet (Vehicles, trailers, trucks)
    PFI = Finance
    ORD = Orders
    TSK = Tasks / Todo
    JRN = Basic activity notes
    CRM = Contacts
    ADR = Adresses
"""

#MAIN LOOP
def main():
    #conn = get_conn()
    #create_database(conn)
    run_cli()

#START
if __name__ == "__main__":
    main()