# Imports
import os
from time import sleep
from util import cheer, alert

# Constants
RATE = 0.05

# File integrity checking
class Check:
    def __init__(self):
        self.paths = [
            "main.py",
            "util.py",
            "engine.py",
            "config.toml",
            "get_config.py",
            "menu.py",
            "packs_viewer.py",
            "packs"
        ]
        self.current_location = os.getcwd()

    def check_file_integrity(self):
        print("Checking file integrity...")
        sleep(RATE + 0.5)
        for path in self.paths:
            print(f"{path}... ", end="")
            sleep(RATE)
            if os.path.exists(os.getcwd() + "\\" + path):
                cheer("Success")
            else:
                alert("Error!")
                return path
