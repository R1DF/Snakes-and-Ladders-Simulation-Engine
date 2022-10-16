# Imports
import questionary
from util import clear, break_line, wait

# Making the app
class Engine:
    def __init__(self, version):
        self.version = version
        self.start_menu_choices = (
            "Play",
            "View packs",
            "Credits",
            "Quit"
        )
        self.selection = -1
        self.main_menu_loop()

    def main_menu_loop(self):
        while True:
            # Always clearing
            clear()

            # Asking for user input
            print(f"Snakes and Ladders Simulation Engine {self.version}")
            print("What would you like to do?\n")

            # Questioning
            self.selection = self.start_menu_choices.index(questionary.select(
                "Select your option:",
                choices=self.start_menu_choices
            ).unsafe_ask())

            # Loading choices
            match self.selection:
                case 2:
                    break_line()
                    print("Made by R1DF. (https://github.com/R1DF/)")
                    print("Coded using Python with questionary and colorama.")
                    print("\nSpecial mention to Adam.")
                    wait()

                case 3:
                    clear()
                    quit()
