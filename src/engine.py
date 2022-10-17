# Imports
import questionary
from util import clear, break_line, wait
from get_config import Config
from packs_viewer import PacksViewer
from packs_detector import get_zipped

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
        self.config_loader = Config("config.toml")

        # Looping
        self.main_menu_loop()  # ALWAYS GO LAST

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
                case 0:
                    break_line()
                    packs = [x["name"] for x in get_zipped()]
                    selected_pack = questionary.select(
                        "Please select a pack (Ctrl+C to cancel):",
                        choices=packs
                    ).ask(kbi_msg="")
                    if selected_pack is not None:
                        pass

                case 1:
                    PacksViewer(self)

                case 2:
                    break_line()
                    print("Made by R1DF. (https://github.com/R1DF/)")
                    print("Coded using Python with questionary and colorama.")
                    print("\nSpecial mention to Adam and Aru.")
                    wait()

                case 3:
                    clear()
                    quit()
