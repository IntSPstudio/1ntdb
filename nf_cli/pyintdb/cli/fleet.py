#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980001035
#|==============================================================|#

#SETTINGS
import click

#MAIN
@click.group(name="flt")
def fleet_group():
    """- Fleet management commands"""
    pass

#REFUELING
@fleet_group.command()
@click.argument('vehicle_id')
def refuel(vehicle_id):
    """- Refuel a vehicle"""
    click.echo(f"Refueling vehicle {vehicle_id}...")
