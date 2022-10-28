# Imports
from colorama import init, Fore, Style
from readchar import readkey
import os

# Colorama must do its thing
init()

# Functions
def get_coloured_message(message):
    return message.replace(
        "~|", Style.RESET_ALL
    ).replace(
        "B#", Fore.BLUE
    ).replace(
        "R#", Fore.RED
    ).replace(
        "Y#", Fore.YELLOW
    ).replace(
        "G#", Fore.GREEN
    ).replace(
        "C#", Fore.CYAN
    ).replace(
        "M#", Fore.MAGENTA
    ).replace(
        "W#", Fore.WHITE
    )


def alert(message):
    print(Fore.RED + message + Style.RESET_ALL)


def inform(message):
    print(Fore.BLUE + message + Style.RESET_ALL)


def notify(message):
    print(Fore.YELLOW + message + Style.RESET_ALL)


def cheer(message):
    print(Fore.GREEN + message + Style.RESET_ALL)


def break_line(amount=1):
    print("\n" * amount)


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def title(program_title):
    if os.name == "nt":
        os.system(f"title {program_title}")  # Windows only


def wait(to_exit=False):
    print(f"Press any key to {'exit' if to_exit else 'continue'}.")
    try:
        readkey()
    except KeyboardInterrupt:
        pass


def pursue_str_input(message="", min_range=None, max_range=None):
    while True:
        user_input = input(f"{message}: ").strip()
        if min_range is not None:
            if len(user_input) < min_range:
                print(f"Please use at least {min_range} characters.\n")
                continue
            elif len(user_input) > max_range:
                print(f"Please use no more than {max_range} characters.\n")
                continue
        return user_input


def pursue_int_input(message="", min_range=None, max_range=None):
    while True:
        user_input = input(f"{message}: ").strip()
        if not user_input.isnumeric():
            print("Please enter a number.\n")
            continue
        user_input = int(user_input)
        if min_range is not None:
            if user_input < min_range:
                print(f"{min_range} is the lowest you can go.\n")
                continue
            elif user_input > max_range:
                print(f"Please enter a number not any higher than {max_range}.\n")
                continue
        return user_input