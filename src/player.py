# Imports
import util
import questionary

# Player class
class Player:
    def __init__(self, master, name):
        # Initialization
        self.master = master
        self.name = name
        self.display_name = name[:self.master.string_representative_width].upper()
        self.coordinates = [0, 0]
        self.redemption_points = 0
        self.has_won = False

    def set_colour(self, colour):
        match colour:
            case "RED":
                self.display_name = f"R#{self.name}~|"
            case "BLUE":
                self.display_name = f"B#{self.name}~|"
            case "YELLOW":
                self.display_name = f"Y#{self.name}~|"
            case "CYAN":
                self.display_name = f"C#{self.name}~|"
            case "MAGENTA":
                self.display_name = f"M#{self.name}~|"
            case "WHITE":
                self.display_name = f"W#{self.name}~|"
            case "GREEN":
                self.display_name = f"G#{self.name}~|"
            case None:
                self.display_name = self.name  # Reset

    def on_inverse_row(self):
        return self.master.must_inverse(self.coordinates[1])

    def use_redemption_point(self):
        prompt = None
        while prompt is None:
            try:
                prompt = questionary.select(
                    "Use 1 Redemption Point?",
                    choices=["Yes", "No"]
                ).unsafe_ask()
                return prompt == "Yes"
            except KeyboardInterrupt:
                continue

    def move(self, units):
        # Getting values and shortening
        grid_width = 10  # Technically a constant but can be replaced in a future update
        grid_height = self.master.pack_data["grid_height"]
        x, y = self.coordinates
        new_x = x + units if not self.on_inverse_row() else x - units

        # Checking whether the player will go up
        goes_up = x + units >= grid_width if not self.on_inverse_row() else x - units < 0
        if goes_up:
            # Checking if the player is on the last row
            if self.coordinates[1] == grid_height - 1:
                print(f"... How unlucky, {self.display_name}. You can't go that far!")
                return

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

        # If the player won...
        if location.coordinates == [grid_height - 1 if (grid_height - 1) % 2 == 0 else 0, grid_height - 1]:
            self.has_won = True
            self.master.winners.append(self.display_name)
            match len(self.master.winners):
                case 1:
                    print(util.get_coloured_message(f"\nG#Congratulations!~|\n{self.display_name} won the game and reacted 1st place!\n"))
                case 2:
                    print(util.get_coloured_message(f"\nG#Well done!~|\n{self.display_name} reached 2nd place!\n"))
                case _:
                    print(util.get_coloured_message(f"\nG#Not bad!~|\n{self.display_name} reached the end!\n"))

            # No need to check further
            return

        # Checking for location type
        match location.location_type:
            case "LADDER":
                if self.master.simulate_question(self, "LADDER"):
                    location.contents.send(self)
            case "SNAKE":
                destination = location.contents.destination
                destination = self.master.field.grid[destination[1]][destination[0]].location_number
                print("\nUh oh... You reached a snake!")
                if self.redemption_points == 0:
                    location.contents.send(self)
                    print(f"You don't have any Redemption Points. You slid down all the way to square {destination}...")
                else:
                    if self.use_redemption_point():
                        self.redemption_points -= 1
                        print("You used 1 Redemption Point. You're safe!")
                    else:
                        location.contents.send(self)
                        print(f"You willingly chose to slide down to square {destination}.")
            case _:
                # Checking for a redemption point
                if location.has_redemption_point:
                    if self.redemption_points < 3:
                        self.master.simulate_question(self, "REDEMPTION")
                    else:
                        print(util.get_coloured_message(f"C#{self.name}~| tried to get a Redemption Point, but was already carrying too many."))


    def surrender(self):
        self.master.active_players.remove(self)
        self.master.surrendered_players.append(self)

    def get_position(self):
        return f"({self.coordinates[0]}, {self.coordinates[1]})"

