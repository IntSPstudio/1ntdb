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

#ADD
@pdb_group.command(name="create")
def create_product():
    """- Add a new product"""
    click.echo("Product wizard...")

#GET BY ID
@pdb_group.command(name="get_id")
@click.argument('product_id', type=int)
def get_product_by_id(product_id):
    """- Get product details by ID"""
    click.echo(f"Getting all from product: {product_id}")

#GET BY REFERENCE
@pdb_group.command(name="get_ref")
@click.argument('product_reference', type=str)
def get_product_by_id(product_reference):
    """- Get product details by reference"""
    click.echo(f"Getting all from product: {product_reference}")    

#GET ALL
@pdb_group.command(name="list")
def get_products():
    """- List of all products"""
    click.echo("Getting all products")