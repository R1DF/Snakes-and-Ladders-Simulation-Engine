# Imports
import os
import toml
from time import sleep
from util import cheer, alert

# Constants
RATE = toml.load(os.getcwd() + "\\config.toml")["constants"]["RATE"] * (2/5)  # shoutout to my math teacher and proportions

# File integrity checking
class Check:
    def __init__(self):
        self.paths = [
            "main.py",
            "util.py",
            "engine.py",
            "game.py",
            "config.toml",
            "get_config.py",
            "menu.py",
            "packs_detector.py",
            "packs_viewer.py",
            "settings_menu.py",
            "field.py",
            "version_checker.py",
            "location.py",
            "sender.py",
            "snake.py",
            "ladder.py",
            "parser.py",
            "packs"
        ]
        self.current_location = os.getcwd()

    def check_file_integrity(self):
        print("Checking file integrity...")
        sleep(RATE + 0.3)
        for path in self.paths:
            print(f"{path}... ", end="")
            sleep(RATE)
            if os.path.exists(os.getcwd() + "\\" + path):
                cheer("Success")
            else:
                alert("Error!")
                return path
