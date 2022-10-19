# Imports (with checks)
try:
    from util import *
    from integrity_check import Check
    from engine import Engine

except ImportError:
    alert("Error importing game files.\nPlease reinstall the game.\n")
    quit()

# CONSTANTS
VERSION = "1.0.0"

# Clearing the screen
clear()
title("Loading...")

# If passed, continue checking
if (missing_file := Check().check_file_integrity()) is not None:
    if missing_file != "packs":
        alert(f"\nThe file {missing_file} is missing.\nPlease reinstall the game.\n\n")
    else:
        alert("\nThe \"packs\" folder inside the game path was not found.\nPlease make it or reinstall the game.\n\n")
    wait(True)
    quit()

# Running
if __name__ == "__main__":
    title(f"Snakes and Ladders Simuation Engine {VERSION}")
    app = Engine(VERSION)
    clear()
