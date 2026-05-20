#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980001035
#|==============================================================|#

#SETTINGS
import click
from pyintdb.cli.journal import journal_group
from pyintdb.cli.fleet import fleet_group
from pyintdb.cli.products import pdb_group

#MAIN
@click.group()
def router():
    """1NTDB: Personal ERP & Inventory System"""
    pass
router.add_command(journal_group)
router.add_command(pdb_group)
router.add_command(fleet_group)

#START COMMAND LINE
def run_cli():
    router()