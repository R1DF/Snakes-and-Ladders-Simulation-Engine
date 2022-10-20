# Imports
import util
import os
import questionary

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

            case "SURRENDER":
                if questionary.confirm(
                    util.get_coloured_message("Are you sure you want to surrender?")
                ).ask():
                    print("loser")
                    util.wait()


