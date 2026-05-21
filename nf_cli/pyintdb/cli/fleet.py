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

#ADDER
@fleet_group.command(name="add")
@click.argument('event', type=str)
@click.argument('target', type=str)
def default_add_event(event, target):
    """- Options: Refuel, service"""
    #REFUEL
    if event == "refuel":
        click.echo(f"Refueling vehicle id: {target}")
    #SERVICE
    if event == "service":
        click.echo(f"Added service event to vehicle id: {target}")
    else:
        click.echo("Invalid event")

#SCHEDULE EVENTS TO FUTURE
@fleet_group.command(name="schedule")
@click.argument('vehicle_id', type=str)
@click.argument('event_type', type=str)
def add_schedule(vehicle_id, event_type):
    """Schedule any future event for a vehicle"""