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

    def on_inverse_row(self):
        return self.master.must_inverse(self.coordinates[1])

    def move(self, units):
        # Getting values and shortening
        grid_width = 10  # Technically a constant but can be replaced in a future update
        grid_height = self.master.pack_data["grid_height"]
        x, y = self.coordinates
        new_x = x + units if not self.on_inverse_row() else x - units

        # Checking whether the player will go up
        goes_up = x + units >= grid_width if not self.on_inverse_row() else x - units < 0
        if goes_up and self.coordinates[1] != grid_height - 1:
            # Cycles - change in Y, Moves - new X but updated depending on row type
            if not self.on_inverse_row():
                cycles = abs(new_x) // grid_height
                moves = abs(new_x - (cycles * grid_height))
            else:
                cycles = (abs(new_x) // grid_height) + 1
                moves = (abs(new_x) % grid_height) - 1

            # Updating
            self.coordinates[1] += cycles
            self.coordinates[0] = moves if not self.on_inverse_row() else self.master.inverse_x_coordinate(moves)

        else:
            # VERY HARD mathematics below (nothing like the previous section)
            self.coordinates[0] = new_x  # very complicated, don't you think?

        # Checking if a special location was reached
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
        return f"({self.coordinates[0]}, {self.coordinates[1]})"

