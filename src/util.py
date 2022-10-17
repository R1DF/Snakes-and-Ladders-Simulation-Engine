# Imports
from colorama import Fore, Style
import os

# Functions
def print_coloured(message):
    pass

def break_line(amount=1):
    print("\n" * amount)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def title(title):
    if os.name == "nt":
        os.system(f"title {title}")  # Windows only

def wait(to_exit=False):
    input(f"Press Enter to {'exit' if to_exit else 'continue'}.\n")