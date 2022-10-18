# Imports
from location import Location

# Field class for every game
class Field:
    def __init__(self, master, pack_data):
        # Attributes
        self.master = master
        self.pack_data = pack_data
        self.width, self.height = self.pack_data["grid"]

        # Getting snakes and ladders (pun not intended) along with their starting coordinates (index: 0)
        self.snakes = self.pack_data["locations"]["snakes"]
        self.snakes_coords = [x["coords"][0] for x in self.snakes]
        self.ladders = self.pack_data["locations"]["ladders"]
        self.ladders_coords = [x["coords"][0] for x in self.ladders]

        # Making the grid
        self.grid = [[Location(self.master, [x, y]) for x in range(self.width)] for y in range(self.height)]  # list comprehensions are incredible

        # Adding all snakes and ladders
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if [x, y] in self.snakes_coords:
                    snake_data = self.snakes[self.snakes_coords.index([x, y])]
                    self.grid[y][x].set_contents("SNAKE", snake_data)

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if [x, y] in self.snakes_coords:
                    ladder_data = self.snakes[self.ladders_coords.index([x, y])]
                    self.grid[y][x].set_contents("LADDER", ladder_data)

