# Imports (with checks)
try:
    from util import *
    from integrity_check import Check
    from engine import Engine

except ImportError as ie:
    alert(f"Error importing game files.\nException message: {ie}\nPlease reinstall the game.\n")
    quit()

# CONSTANTS
VERSION = "1.0.0"

# Clearing the screen
clear()
title("Loading...")

# If passed, continue checking
try:
    if (missing_file := Check().check_file_integrity()) is not None:
        if missing_file != "packs":
            alert(f"\nThe file {missing_file} is missing.\nPlease reinstall the game.\n\n")
        else:
            alert("\nThe \"packs\" folder inside the game path was not found.\nPlease make it or reinstall the game.\n\n")
        wait(True)
        quit()
except KeyboardInterrupt:
    break_line()
    notify("Integrity check skipped.\nHINT: You can disable integrity checks with the settings file.")
    wait()

# Running
if __name__ == "__main__":
    try:
        app = Engine(VERSION)
        clear()
    except KeyboardInterrupt:
        clear()
        notify("Game force quitted.")
        wait(True)
        quit()

