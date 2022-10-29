# Imports (with checks)
try:
    from util import *
    from integrity_check import Check
    from engine import Engine
    from get_config import Config
    should_check_integrity = Config("config.toml").data["program"]["CHECK_FILE_INTEGRITY"]

except ImportError as ie:
    alert(f"Error importing game files.\nException message: {ie}\nPlease reinstall the game.")
    wait(True)
    quit()

except FileNotFoundError as fnfe:
    alert(f"Error searching for the configuration file.\nException message: {fnfe}\nPlease reinstall the game.")
    wait(True)
    quit()

except Exception as e:
    alert(f"Ran into unexpected exception.\nException message: {e}\nPlease reinstall the game.\nIf the error persists, "
          f"submit an issue at https://github.com/R1DF/Snakes-and-Ladders-Simulation-Engine about your error.")
    wait(True)
    quit()

# CONSTANTS
VERSION = "1.0.0"

# Clearing the screen
clear()
title("Loading...")

# If passed, continue checking
if should_check_integrity:
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
        notify("Integrity check skipped.\nHINT: You can disable integrity checks in the settings menu.")
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

