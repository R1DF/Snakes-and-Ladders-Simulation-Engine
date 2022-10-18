# Importing Snakes and Ladders objects
from snake import Snake
from ladder import Ladder

# Location class
class Location:
    def __init__(self, master, coordinates):
        # Initialization
        self.master = master
        self.coordinates = coordinates
        self.has_redemption_point = False

        # Contents
        self.contents = None

    def set_contents(self, location_type, data):
        match location_type:
            case "SNAKE":
                self.contents = Snake(self.master, data)
            case "LADDER":
                self.contents = Ladder(self.master, data)

    def add_redemption_point(self):
        self.has_redemption_point = True

