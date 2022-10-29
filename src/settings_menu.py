# Base import
import os
import toml
import copy
import questionary
from menu import BaseMenu
from util import title, clear, wait, pursue_float_input, pursue_yn_input, break_line

# Settings viewer class
class SettingsMenu(BaseMenu):
    def __init__(self, master):
        # Getting TOML data
        self.original_data = toml.load(os.getcwd() + "\\config.toml")
        self.current_data = copy.deepcopy(self.original_data)

        # Loading time
        BaseMenu.__init__(self, master)

    def print_data(self, data):
        will_check_file_integrity, rate_of_loading = data["program"]["CHECK_FILE_INTEGRITY"], data["constants"]["RATE"] * 1000
        print("Check file integrity:", "Yes" if will_check_file_integrity else "No")
        print(f"Loading rate: {rate_of_loading}ms")

    def save_changes(self):
        print("Loading...")
        toml.dump(self.current_data, open(os.getcwd() + "\\config.toml", "w"))
        print("Changes saved.\nNOTE: Your changes will only come to effect next startup (without force restarts).")

    def is_different(self):
        return self.original_data != self.current_data

    def load(self):
        title(f"Snakes and Ladders Engine v{self.master.version} - Settings")

        # Menu specific
        self.has_saved = False
        self.changing_options = [
            "Checking file integrity",
            "Loading time rate per iterable",
            "Save changes",
            "Exit"
        ]

        # Setting sloop
        while True:
            # Printing out the defaults
            clear()
            print("Your current settings:")
            self.print_data(self.current_data)
            if self.is_different() and (not self.has_saved):
                print("Your changes aren't saved.")
            break_line()

            # Changing options query
            print("What would you like to change?")
            choice = questionary.select(
                "Select your option:",
                choices=self.changing_options
            ).unsafe_ask()

            match self.changing_options.index(choice):
                case 0:
                    choice = pursue_yn_input("Check file integrity on startup?")
                    self.current_data["program"]["CHECK_FILE_INTEGRITY"] = choice
                    self.has_saved = False

                case 1:
                    choice = pursue_float_input("Enter amount of milliseconds", min_range=0.002, max_range=0.9)
                    self.current_data["constants"]["RATE"] = choice / 1000
                    self.has_saved = False

                case 2:
                    break_line()
                    self.save_changes()
                    self.has_saved = True
                    wait()

                case 3:
                    break

