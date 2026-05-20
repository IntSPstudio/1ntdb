#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980001035
#|==============================================================|#

#SETTINGS
import click
from datetime import datetime

#MAIN
@click.group(name="jrn")
def journal_group():
    """- Journal entries for logging all events and thoughts"""
    pass

#BASIC ADDER
@journal_group.command(name="add")
@click.argument('text', type=str)
@click.option('--target', '-t', type=str, help="Optional target id")
def add_basic_note(text, target):
    """Add a quick time-stamped note to the system"""
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if target:
        click.echo(f"[{now}] : {text} : {target}")
    else:
        click.echo(f"[{now}] : {text}")