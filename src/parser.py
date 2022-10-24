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

            case "ROLL":
                print("Throwing the die...")
                roll = random.randint(1, self.master.pack_data["die_faces"])
                print(f"{player.name} rolled a {roll}!")
                player.move(roll)
                return True

            case "PLAYERS":
                print("Loading map...")
                data = self.master.field.show_players()
                for player_name, player_coordinates in data:
                    location_string_coloured = self.master.field.grid[player_coordinates[1]][player_coordinates[0]].location_string_coloured
                    print(util.get_coloured_message(f"{player_name} is located at square {location_string_coloured}."))
                util.break_line()

            case "LOCATIONS":
                print("Loading map...")
                self.master.field.show_points(player)
                print(f"\nYou're at square {int(self.master.field.grid[player.coordinates[1]][player.coordinates[0]].location_string)}.")
                print("\n# - Ladder\nS - Snake\n* - Redemption Point\n\nColoured number squares are destinations of their corresponding snake/ladder.\n")

            case "STATUS":
                player_position = int(self.master.field.grid[player.coordinates[1]][player.coordinates[0]].location_string)
                distance = (self.master.pack_data["grid_height"] * 10) - player_position
                print(f"You are {distance} unit{'s' if distance > 1 else ''} away from the finishing point.\nPosition: Square {player_position}, {player.get_position()}")
                util.break_line()

            case "SURRENDER":
                if questionary.confirm(
                    util.get_coloured_message("Are you sure you want to surrender?")
                ).ask():
                    print("loser")
        return False

