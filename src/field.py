# Imports
import util
from location import Location

# Field class for every game
class Field:
    def __init__(self, master, pack_data):
        # Attributes
        self.master = master
        self.pack_data = pack_data
        self.width, self.height = 10, self.pack_data["grid_height"]

        # Getting snakes and ladders (pun not intended) along with their starting coordinates (index: 0)
        self.snakes = self.pack_data["locations"]["snakes"]
        self.snakes_coordinates = [x["coords"][0] for x in self.snakes]
        self.ladders = self.pack_data["locations"]["ladders"]
        self.ladders_coordinates = [x["coords"][0] for x in self.ladders]

        # Getting redemption point coordinates
        self.redemption_point_coordinates = self.pack_data["locations"]["redemption_points"]["coordinates"]

        # Creating containers
        self.snake_objects = []
        self.ladder_objects = []
        self.redemption_points = []

        # Getting colours
        self.all_colours = [
            "RED",
            "BLUE",
            "MAGENTA",
            "CYAN",
            "WHITE",
            "GREEN"
        ]

        # Making the grid
        self.grid = [[Location(self, [x, y]) for x in range(self.width)] for y in range(self.height)]  # list comprehensions are incredible

        # Adding all snakes and ladders
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if [x, y] in self.snakes_coordinates:
                    snake_data = self.snakes[self.snakes_coordinates.index([x, y])]
                    self.snake_objects.append(self.grid[y][x])
                    self.grid[y][x].set_contents("SNAKE", snake_data)

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if [x, y] in self.ladders_coordinates:
                    ladder_data = self.ladders[self.ladders_coordinates.index([x, y])]
                    self.ladder_objects.append(self.grid[y][x])
                    self.grid[y][x].set_contents("LADDER", ladder_data)

        # Colouring all snakes and ladders as well
        for snake_index in range(len(self.snake_objects)):
            colour = self.all_colours[snake_index % (len(self.all_colours) - 1)]
            snake_object = self.snake_objects[snake_index].contents
            snake_object.set_colour(colour)
            self.grid[snake_object.destination[1]][snake_object.destination[0]].set_colour(colour)

        for ladder_index in range(len(self.ladder_objects)):
            colour = self.all_colours[ladder_index % (len(self.all_colours) - 1)]
            ladder_object = self.ladder_objects[ladder_index].contents
            ladder_object.set_colour(colour)
            self.grid[ladder_object.destination[1]][ladder_object.destination[0]].set_colour(colour)

        # Setting and colouring redemption points
        for redemption_point in self.redemption_point_coordinates:
            self.grid[redemption_point[1]][redemption_point[0]].add_redemption_point()

    def show_points(self):
        # Getting formatted points
        printed_grid = []
        for y in range(len(self.grid)):
            printed_grid.append([util.get_coloured_message(x.get_display_name()) for x in self.grid[y][::]])

        # Printing out the formatted points and printing out the lists in reverse
        for row in printed_grid[::-1]:
            print(" | ".join(row))
