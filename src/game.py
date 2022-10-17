# Imports
import os
import json

# Game class
class SnakesAndLadders:
    def __init__(self, pack_file_name):
        # Initialization and loading
        self.pack_file_name = pack_file_name
        self.pack_data = json.load(open(os.getcwd() + "\\packs\\" + self.pack_file_name, "r"))

        """
        Grid information:
        NONE - The place is empty.
        REDEMPTION - Redemption point available.
        SNAKETO[XY] - Snake location that moves the player to the specified spot.
        LADDERTO[XY] - Ladder location that moves the player to the specified spot.
        """

        # Loading grid
        self.grid_width, self.grid_height = self.pack_data["grid"]
        self.grid = [["NONE" for x in range(self.grid_width)] for y in range(self.grid_height)]
        print(self.grid)

        # Getting snakes and ladders
        self.snakes, self.ladders = self.pack_data["locations"]["snakes"], self.pack_data["locations"]["ladders"]
        self.snakes_locations, self.ladders_locations = [x["coords"][0] for x in self.snakes], [x["coords"][0] for x in self.ladders]




if __name__ == "__main__":
    SnakesAndLadders("interwar_europe.json")