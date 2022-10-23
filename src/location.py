# Importing Snakes and Ladders objects
from snake import Snake
from ladder import Ladder

# Location class
class Location:
    def __init__(self, master, coordinates):
        # Initialization
        self.master = master
        self.coordinates = coordinates
        self.location_string = None
        self.has_redemption_point = False

        # Contents
        self.contents = None

        # Setting the location string
        self.set_location_string()

    def set_contents(self, location_type, data):
        match location_type:
            case "SNAKE":
                self.contents = Snake(self.master, data)
            case "LADDER":
                self.contents = Ladder(self.master, data)

    def set_location_string(self):
        # LOGIC ERROR: doesn't work when X is stretched beyond or less than 10
        is_not_end = self.coordinates[0] != self.master.width - 1
        if self.coordinates[1] == 0:  # If the location is in the 0th row
            row_index = 0 if self.coordinates[0] < self.master.width - 1 else 1  # An extra 0 is added
        else:  # Otherwise
            row_index = self.coordinates[1] if is_not_end else self.coordinates[1] + 1
        self.location_string = f"{row_index}{self.coordinates[0] + 1 if is_not_end else '0'}"

    def add_redemption_point(self):
        self.has_redemption_point = True

    def get_display_name(self):
        if self.contents is not None:
            return self.contents.display_name
        elif self.has_redemption_point:
            return "X" * self.master.master.string_representative_width
        else:
            return self.location_string

