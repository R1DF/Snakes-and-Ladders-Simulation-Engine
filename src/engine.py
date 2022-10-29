# Imports
import questionary
import json
import os
from game import SnakesAndLadders
from util import clear, break_line, wait, pursue_str_input, pursue_int_input, title
from get_config import Config
from settings_menu import SettingsMenu
from packs_viewer import PacksViewer
from packs_detector import get_zipped
from version_checker import CheckVersion

# Making the app
class Engine:
    def __init__(self, version):
        self.version = version
        self.start_menu_choices = (
            "Play",
            "Packs",
            "Settings",
            "Credits",
            "Check for updates (internet required)",
            "Quit"
        )
        self.selection = -1
        self.config_loader = Config("config.toml")

        # Looping
        self.main_menu_loop()  # ALWAYS GO LAST

    def main_menu_loop(self):
        while True:
            # Always clearing
            title(f"Snakes and Ladders Simuation Engine v{self.version}")
            clear()

            # Asking for user input
            print(f"Snakes and Ladders Simulation Engine v{self.version}")
            print("Made by R1DF.\n")

            # Questioning
            self.selection = self.start_menu_choices.index(questionary.select(
                "Select your option:",
                choices=self.start_menu_choices
            ).unsafe_ask())

            # Loading choices
            match self.selection:
                case 0:
                    break_line()
                    file_names = [x["file_name"] for x in get_zipped()]
                    packs = [x["name"] for x in get_zipped()]
                    selected_pack = questionary.select(
                        "Please select a pack (Ctrl+C to cancel):",
                        choices=packs
                    ).unsafe_ask()
                    selected_pack_file_name = file_names[packs.index(selected_pack)]
                    if selected_pack is not None:
                        print("Fetching player limit...")
                        player_limit = json.load(open(os.getcwd() + "\\packs\\" + selected_pack_file_name))["player_limit"]
                        player_names = []
                        # Logic error possibility: if 2 packs are equally named
                        print(f"This pack allows a maximum of {player_limit} players.\n")
                        for player in range(pursue_int_input(f"Enter amount of players (2-{player_limit})", 2, player_limit)):
                            while True:
                                player_name = pursue_str_input(f"Enter name for player {player + 1}", 3, 10)
                                if player_name.lower() in [x.lower() for x in player_names]:
                                    print("Enter another player name.\n")
                                    continue
                                player_names.append(player_name)
                                break
                        self.game = SnakesAndLadders(self.version, selected_pack_file_name, player_names)
                        wait()
                case 1:
                    PacksViewer(self)

                case 2:
                    SettingsMenu(self)

                case 3:
                    break_line()
                    print("Made by R1DF. (https://github.com/R1DF/)")
                    print("Coded using Python with questionary and colorama.")
                    print("\nSpecial mention to Adam and Aru.")
                    wait()

                case 4:
                    break_line()
                    CheckVersion().check(self.version)
                    wait()

                case 5:
                    clear()
                    quit()
