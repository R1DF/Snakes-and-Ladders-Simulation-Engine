# Imports
import util

# Player class
class Player:
    def __init__(self, master, name):
        # Initialization
        self.master = master
        self.name = name
        self.coordinates = [0, 0]
        self.redemption_points = 0

    def move(self, units):
        grid_width = 10  # Technically a constant but can be replaced in a future update
        grid_height = self.master.pack_data["grid_height"]

        # Checking positioning
        if self.coordinates[0] + units >= grid_height:  # Determines if the player moves up or not
            if self.coordinates[1] != grid_height - 1:  # Can't move further if you're at the top
                cycles = (self.coordinates[0] + units) // 10
                moves = self.coordinates[0] + units - (cycles * 10)
                self.coordinates[0] = moves
                self.coordinates[1] += cycles
        else:
            if self.coordinates[0] + units <= grid_width:
                self.coordinates[0] += units

        location = self.master.field.grid[self.coordinates[1]][self.coordinates[0]]

        # Checking for location type
        match location.location_type:
            case "LADDER":
                pass
            case "SNAKE":
                pass
            case _:
                # Checking for a redemption point
                if location.has_redemption_point:
                    if self.redemption_points < 3:
                        if self.master.simulate_question(self, "REDEMPTION"):
                            print(util.get_coloured_message(f"G#Correct!~|\nC#{self.name}~| received a M~Redemption Point~|!"))
                            self.redemption_points += 1
                            location.has_redemption_point = False
                        else:
                            print(util.get_coloured_message(f"R#Incorrect!~|\nC#{self.name}~| tried to receive a M#Redemption Point~|, but failed..."))
                    else:
                        print(util.get_coloured_message(f"C#{self.name}~| tried to get a Redemption Point, but was already carrying too many."))



    def get_position(self):
        return f"({self.coordinates[0] + 1}, {self.coordinates[1] + 1})"

