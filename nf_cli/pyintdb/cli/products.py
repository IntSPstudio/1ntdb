#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980001035
#|==============================================================|#

#SETTINGS
import click

#MAIN
@click.group(name="pdb")
def pdb_group():
    """- Product database commands"""
    pass

#CREATE NEW PRODUCT
@pdb_group.command(name="create")
def create_product():
    """- Add a new product via wizard"""
    click.echo("Product wizard...")

#GET
@pdb_group.command(name="get")
@click.argument('select', type=str)
@click.argument('target', required=False)
def default_add_event(select, target):
    """- Options: all, id, ref"""
    #ALL
    if select == "all":
        click.echo("Getting all products")
    #BY ID
    elif select == "id":
        click.echo(f"Getting all from product by ID: {target}")
    #BY REFERENCE
    elif select == "ref":
        click.echo(f"Getting all from product by REFERENCE: {target}")
    #
    else:
        click.echo("Invalid option")