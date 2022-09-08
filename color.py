from enum import Enum

class color_type(Enum):
    purple = 0
    blue   = 1
    green  = 2
    yellow = 3
    orange = 4
    red    = 5

def color_to_text(color):
    switcher = {
        color_type.purple: 'purple',
        color_type.blue: 'blue',
        color_type.green: 'green',
        color_type.yellow: 'yellow',
        color_type.orange: 'orange',
        color_type.red: 'red',
    }
    return switcher.get(color, "Invalid color")
