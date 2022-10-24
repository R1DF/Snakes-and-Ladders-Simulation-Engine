# Imports
import os
import json
import random
import util
from field import Field
from player import Player
from parser import Parser

# Constants
VALID_COMMANDS = (
    "HELP",
    "CLEAR",
    "ROLL",
    "PLAYERS",
    "LOCATIONS",
    "STATUS",
    "SURRENDER"
)

VERY_NAUGHTY_WORDS = (
    "FUCK",
    "SHIT",
    "BITCH",
    "PUSSY",
    "COCK",
    "SEX"
)

# Game class
class SnakesAndLadders:
    def __init__(self, pack_file_name, player_names, debug=False):
        # Initialization and loading
        self.pack_file_name = pack_file_name
        self.pack_data = json.load(open(os.getcwd() + "\\packs\\" + self.pack_file_name, "r"))
        self.has_anyone_won = False
        self.players = []
        """
        Grid information:
        NONE - The place is empty.
        REDEMPTION - Redemption point available.
        SNAKETO[XY] - Snake location that moves the player to the specified spot.
        LADDERTO[XY] - Ladder location that moves the player to the specified spot.
        """

        # Loading grid
        self.grid_width, self.grid_height = 10, self.pack_data["grid_height"]
        self.string_representative_width = len(str(self.grid_width * self.grid_height))
        self.field = Field(self, self.pack_data)

        # Creating players
        player_names_shuffled = player_names.copy()
        random.shuffle(player_names_shuffled)
        for player_name in player_names_shuffled:
            self.players.append(Player(self, player_name))

        # Parser + Game loop
        self.parser = Parser(self)

        if not debug:
            self.initiate_loop()

    def initiate_loop(self):
        counter = 0
        while not self.has_anyone_won:
            counter += 1
            for player in self.players:
                util.clear()
                player_name = player.name
                has_valid_command = False

                print(util.get_coloured_message(
                    f"M#Turn {counter}~|\nM#Current player: {player_name}~|\nEnter B#HELP~| for a list of commands.")
                )

                while not has_valid_command:
                    command = util.pursue_str_input(util.get_coloured_message("Enter command"))
                    if command == "":
                        util.alert("ERROR: No command given.")
                        util.break_line()
                        continue

                    elif any(x in VERY_NAUGHTY_WORDS for x in command.upper().strip().split()):
                        util.alert("ERROR: Watch your mouth.")
                        util.break_line()
                        continue

                    elif command.upper() not in VALID_COMMANDS:
                        util.alert("ERROR: Invalid command.")
                        util.break_line()
                        continue

                    else:
                        util.break_line()
                        has_valid_command = self.parser.parse(command.upper(), player)

                util.wait()

    def inverse_x_coordinate(self, x):
        return abs(self.grid_width - 1 - x)  # using Real Coordinate System (grid width begins from 0)

    def simulate_question(self, player, which_type):
        match which_type:
            case "REDEMPTION":
                question = self.pack_data["redemption_point_questions"]

    def must_inverse(self, row):
        return row % 2 != 0

if __name__ == "__main__":
    a = SnakesAndLadders("test.json", ["John"])
    # a.field.show_points()
    # a = a.field.grid
    # for x in a[::-1]:
    #     print([y.coordinates for y in x])

