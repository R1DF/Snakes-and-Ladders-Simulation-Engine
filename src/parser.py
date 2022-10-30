# Imports
import util
import os
import questionary
import random

# Constants
HELP_FILE = util.get_coloured_message(open(os.getcwd() + "\\txt\\instructions.txt").read())


# Parser class
class Parser:
    def __init__(self, master):
        self.master = master

    def parse(self, command, player):
        match command:
            case "HELP":
                print(HELP_FILE)

            case "CLEAR":
                util.clear()
                print(util.get_coloured_message(f"M#Current player: {player.name}~|\n"))

            case "ROLL" | "MOVE":
                print("Throwing the die...")
                roll = random.randint(1, self.master.pack_data["die_faces"])
                print(f"{player.name} rolled a {roll}!")
                player.move(roll)
                return True

            case "PLAYERS":
                print("Loading map...")
                data = self.master.field.show_players()
                for player_name, player_coordinates in data:
                    location_string_coloured = self.master.field.grid[player_coordinates[1]][
                        player_coordinates[0]].location_string_coloured
                    print(util.get_coloured_message(f"{player_name} is located at square {location_string_coloured}."))
                util.break_line()

            case "LOCATIONS" | "WHERE" | "MAP":
                print("Loading map...")
                self.master.field.show_points(player)
                print(
                    f"\nYou're at square {int(self.master.field.grid[player.coordinates[1]][player.coordinates[0]].location_string)}.")
                print(
                    "\n# - Ladder\nS - Snake\n* - Redemption Point\n\nColoured number squares are destinations of their corresponding snake/ladder.\n")

            case "STATUS" | "DISTANCE":
                player_position = int(
                    self.master.field.grid[player.coordinates[1]][player.coordinates[0]].location_string)
                distance = (self.master.pack_data["grid_height"] * 10) - player_position
                print(
                    f"You are {distance} unit{'s' if distance > 1 else ''} away from the finishing point.\nPosition: Square {player_position}, {player.get_position()}")
                util.break_line()

            case "INSPECT SNAKE":
                snake_number = util.pursue_int_input("Enter square number of the snake", min_range=1,
                                                     max_range=self.master.grid_width * self.master.grid_height)
                snake_coords = self.master.get_coordinates_from_square_number(snake_number)

                if self.master.field.grid[snake_coords[1]][snake_coords[0]].location_type != "SNAKE":
                    util.alert("That square does not have a snake head.")
                else:
                    destination_coordinates = self.master.field.grid[snake_coords[1]][
                        snake_coords[0]].contents.destination
                    destination_object = self.master.field.grid[destination_coordinates[1]][destination_coordinates[0]]
                    print(util.get_coloured_message(
                        f"This snake's destination is square {destination_object.location_string_coloured}."))
                util.break_line()

            case "INSPECT LADDER":
                ladder_number = util.pursue_int_input("Enter square number of the ladder", min_range=1,
                                                      max_range=self.master.grid_width * self.master.grid_height)
                ladder_coords = self.master.get_coordinates_from_square_number(ladder_number)

                if self.master.field.grid[ladder_coords[1]][ladder_coords[0]].location_type != "LADDER":
                    util.alert("That square does not have a ladder on it.")
                else:
                    destination_coordinates = self.master.field.grid[ladder_coords[1]][
                        ladder_coords[0]].contents.destination
                    destination_object = self.master.field.grid[destination_coordinates[1]][destination_coordinates[0]]
                    print(util.get_coloured_message(
                        f"This ladder's destination is square {destination_object.location_string_coloured}."))
                util.break_line()

            case "SURRENDER":
                if questionary.confirm(
                        util.get_coloured_message("Are you sure you want to surrender?")
                ).ask():
                    player.surrender()
                    print(util.get_coloured_message(f"{player.display_name} surrendered. What a shame."))
                    return True
        return False
