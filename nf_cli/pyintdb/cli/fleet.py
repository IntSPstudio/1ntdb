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
@fleet_group.command(name="refuel")
@click.argument('vehicle_id')
def add_refuel_event(vehicle_id):
    """- Refuel a vehicle"""
    click.echo(f"Refueling vehicle {vehicle_id}...")

#SCHEDULE EVENTS
@fleet_group.command(name="schedule")
@click.argument('vehicle_id', type=str)
@click.argument('event_type', type=str)
def add_schedule(vehicle_id, event_type):
    """Schedule any future event for a vehicle"""