# Imports
import os
import json
import random
import util
import questionary
from field import Field
from player import Player
from parser import Parser

# Constants
VALID_COMMANDS = (
    "HELP",
    "CLEAR",
    "ROLL",
    "MOVE",
    "PLAYERS",
    "LOCATIONS",
    "WHERE",
    "MAP",
    "STATUS",
    "DISTANCE",
    "INSPECT SNAKE",
    "INSPECT LADDER",
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
    def __init__(self, version, pack_file_name, player_names, debug=False):
        # Initialization and loading
        util.title(f"Snakes and Ladders Simulation Engine v{version} - Game in session")
        self.pack_file_name = pack_file_name
        self.pack_data = json.load(open(os.getcwd() + "\\packs\\" + self.pack_file_name, "r"))
        self.players = []
        self.winners = []

        # Making constant
        self.players_colours = (
            "RED",
            "BLUE",
            "YELLOW",
            "GREEN",
            "CYAN",
            "MAGENTA"
        )

        # Loading grid
        self.grid_width, self.grid_height = 10, self.pack_data["grid_height"]
        self.string_representative_width = len(str(self.grid_width * self.grid_height))
        self.field = Field(self, self.pack_data)

        # Creating players and adding their colours
        player_names_shuffled = player_names.copy()
        random.shuffle(player_names_shuffled)
        for player_index in range(len(player_names_shuffled)):
            self.players.append(Player(self, player_names_shuffled[player_index]))
            self.players[player_index].set_colour(self.players_colours[player_index % len(self.players_colours)])

        # Getting active players
        self.active_players = self.players.copy()
        self.surrendered_players = []

        # Parser + Game loop
        self.parser = Parser(self)

        if not debug:
            util.title(f"Snakes and Ladders Simulation Engine v{version} - Game ongoing")
            turns = self.initiate_loop()

            # After the game is over
            util.clear()
            util.title(f"Snakes and Ladders Simulation Engine v{version} - Game ended")
            print(f"Great game. Here's the statistics below:\n\nAmount of turns: {turns}")

            # Getting out the scorings and finding out who surrendered and who did not
            if not self.active_players:
                print("Wow. Everyone surrendered. No-one wins.\n\nPlayers:")
                for player in self.surrendered_players:
                    print(util.get_coloured_message(f"{player.display_name}"))

            elif len(self.active_players) == 1:
                print(util.get_coloured_message(f"The winner is {self.winners[0]}!\nEveryone else surrendered.\n\nSurrendered:"))
                for player in self.surrendered_players:
                    print(util.get_coloured_message(f"{player.display_name}"))
            else:
                for player_index, player in enumerate(self.winners):
                    print(util.get_coloured_message(f"{player_index + 1}. {player}"))
                print("\nSurrendered:")
                for player in self.surrendered_players:
                    print(util.get_coloured_message(player.display_name))
            util.break_line()


    def initiate_loop(self):
        counter = 0
        while not all(x.has_won for x in self.active_players):
            counter += 1
            for player in self.active_players:
                # Always skip players that won
                if player.has_won:
                    continue

                # Otherwise
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
        return counter

    def inverse_x_coordinate(self, x):
        return abs(self.grid_width - 1 - x)  # using Real Coordinate System (grid width begins from 0)

    def get_coordinates_from_square_number(self, number):
        y = (number - 1) // self.grid_width
        x = (number - (self.grid_width * y)) - 1
        if self.must_inverse(y):
            x = self.inverse_x_coordinate(x)
        print(x, y)
        return [x, y]

    def simulate_question(self, player, which_type):
        match which_type:
            case "LADDER":
                # Setting up question
                location_contents = self.field.grid[player.coordinates[1]][player.coordinates[0]].contents
                question = random.choice(location_contents.data["questions"])
                correct_answer = question["answers"][0]
                answers = question["answers"].copy()
                random.shuffle(answers)

                # Introducing the question
                util.break_line()
                print(f"{player.name} reached a ladder.\nAnswer the question below correctly to skip through.\n")
                prompt = None
                while prompt is None:
                    try:
                        prompt = questionary.select(
                            question["question"],
                            choices=answers
                        ).unsafe_ask()
                        break
                    except KeyboardInterrupt:
                        continue

                # Checking question validity
                if prompt == correct_answer:
                    destination = location_contents.destination
                    destination = self.field.grid[destination[1]][destination[0]].location_number
                    print(util.get_coloured_message(f"\nG#Correct!~|\nYou are now at square {destination}!"))
                    return True
                else:
                    print(util.get_coloured_message(f"\nR#Incorrect!~|\nToo bad. The correct answer was \"{correct_answer}\"!"))
                    return False

            case "REDEMPTION":
                # Setting up question
                question = random.choice(self.pack_data["locations"]["redemption_points"]["questions"])
                correct_answer = question["answers"][0]
                answers = question["answers"].copy()
                random.shuffle(answers)

                # Introducing the question
                util.break_line()
                print(f"{player.name}, congratulations! You reached a Redemption Point!\nAnswer the question below correctly to earn it!\n")
                prompt = None
                while prompt is None:
                    try:
                        prompt = questionary.select(
                            question["question"],
                            choices=answers
                        ).unsafe_ask()
                        break
                    except KeyboardInterrupt:
                        continue

                # Checking question validity
                if prompt == correct_answer:
                    self.field.grid[player.coordinates[1]][player.coordinates[0]].delete_redemption_point()
                    player.redemption_points += 1
                    print(util.get_coloured_message(f"\nG#Correct!~|\n{player.display_name} now has {player.redemption_points} Redemption Point{'' if player.redemption_points == 1 else 's'}."))
                else:
                    print(util.get_coloured_message(f"\nR#Incorrect!~|\nToo bad. The correct answer was \"{correct_answer}\"!"))


    def must_inverse(self, row):
        return row % 2 != 0

if __name__ == "__main__":
    pass
    # a = SnakesAndLadders("test.json", ["John"], True)
    # a.field.show_points()
    # a = a.field.grid
    # for x in a[::-1]:
    #     print([y.coordinates for y in x])

