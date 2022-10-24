# Importing Snakes and Ladders objects
from snake import Snake
from ladder import Ladder
import util

# Location class
class Location:
    def __init__(self, master, coordinates):
        # Initialization
        self.master = master
        self.coordinates = coordinates
        self.location_type = "NORMAL"
        self.location_number = None
        self.location_string = None
        self.location_string_coloured = None
        self.has_redemption_point = False

        # Contents
        self.contents = None

        # Setting the location string
        self.set_location_number()

    def set_contents(self, location_type, data):
        match location_type:
            case "SNAKE":
                self.location_type = "SNAKE"
                self.contents = Snake(self, data)
            case "LADDER":
                self.location_type = "LADDER"
                self.contents = Ladder(self, data)

    def set_colour(self, colour):
        match colour:
            case "RED":
                self.location_string_coloured = f"R#{self.location_string}~|"
            case "BLUE":
                self.location_string_coloured = f"B#{self.location_string}~|"
            case "YELLOW":
                self.location_string_coloured = f"Y#{self.location_string}~|"
            case "CYAN":
                self.location_string_coloured = f"C#{self.location_string}~|"
            case "MAGENTA":
                self.location_string_coloured = f"M#{self.location_string}~|"
            case "WHITE":
                self.location_string_coloured = f"W#{self.location_string}~|"
            case "GREEN":
                self.location_string_coloured = f"G#{self.location_string}~|"
            case None:
                self.location_string_coloured = self.location_string  # Reset

    def set_location_number(self):
        # Uses its coordinates to find the number (wy + x, w = width)
        current_row_unit = self.coordinates[0] + 1 if not self.on_inverse_row() else self.master.master.inverse_x_coordinate(self.coordinates[0]) + 1
        self.location_number = current_row_unit + (self.master.width * self.coordinates[1])

        # Location string obtained differently
        self.location_string = f"{'0' * (self.master.master.string_representative_width - len(str(self.location_number)))}{self.location_number}"
        self.location_string_coloured = f"W#{self.location_string}~|"

    def add_redemption_point(self):
        self.has_redemption_point = True
        self.set_colour("YELLOW")

    def delete_redemption_point(self):
        self.has_redemption_point = False
        self.set_colour(None)

    def on_inverse_row(self):
        return self.coordinates[1] % 2 != 0

    def get_display_name(self):
        if self.contents is not None:
            return self.contents.display_name
        elif self.has_redemption_point:
            return util.get_coloured_message(f"Y#{'*' * self.master.master.string_representative_width}~|")
        else:
            return self.location_string_coloured

