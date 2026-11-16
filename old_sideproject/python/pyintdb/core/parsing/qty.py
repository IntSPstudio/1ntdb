#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this project!
# ID: 980002035
#|==============================================================|#

#SETTINGS
import re

#SEPARATE VALUES AND UNITS
def parse_qty_input(value: str):
    match = re.match(r"^\s*(\d+(?:[.,]\d+)?)\s*([a-zA-Z]+)\s*$", value)
    
    if not match:
        raise ValueError(f"Invalid qty format: {value}")
    
    qty = float(match.group(1).replace(",", "."))
    unit = match.group(2).lower()

    return qty, unit