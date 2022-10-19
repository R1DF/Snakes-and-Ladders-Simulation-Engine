# Imports
import os
import json
import random
from field import Field
from player import Player

# Game class
class SnakesAndLadders:
    def __init__(self, pack_file_name, player_names):
        # Initialization and loading
        self.pack_file_name = pack_file_name
        self.pack_data = json.load(open(os.getcwd() + "\\packs\\" + self.pack_file_name, "r"))
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
        self.field = Field(self, self.pack_data)

        # Creating players
        player_names_shuffled = player_names.copy()
        random.shuffle(player_names_shuffled)
        for player_name in player_names_shuffled:
            self.players.append(Player(self, player_name))

        # Getting snakes and ladders
        self.snakes, self.ladders = self.pack_data["locations"]["snakes"], self.pack_data["locations"]["ladders"]
        self.snakes_locations, self.ladders_locations = [x["coords"][0] for x in self.snakes], [x["coords"][0] for x in self.ladders]


if __name__ == "__main__":
    SnakesAndLadders("test2.json", ["Albert", "Adam", "Adrian"]).field.show_points()

