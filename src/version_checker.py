# Imports
import requests
import util
from urllib.request import urlopen

# Class blueprint
class CheckVersion:
    def check(self, version):
        # Dummy internet test
        util.notify("Checking for internet connection...")
        try:
            urlopen("https://httpstat.us/200")
            util.cheer("Success.\n")
        except Exception:
            util.alert("\nTest connection failed!"
                       "\nAre you connected to internet?"
                       "\nIf yes, please check it yourself as an error occurred connecting."
                       "\nLink: https://github.com/R1DF/Snakes-and-Ladders-Simulation-Engine\n")
            return

        # Connecting to online data with URL
        util.notify("Connecting to online version data...")
        try:
            latest_version = requests.get("https://r1df.github.io/version_check.json")
            if latest_version.status_code != 200: # If there's a non-OK status code
                util.alert("Failed to connect!")
                print(f"HTTP code: {latest_version.status_code}\n")
                match latest_version.status_code:
                    case 404:
                        print("The versioning website was not found.")
                    case 403 | 401:
                        print("Access isn't allowed.")
                    case 451:
                        print("I got Ace Attorney'd.")
                    case 500:
                        print("There's an error with the server that this program can't fix.")
                print("For more information, please search about the error's status code."
                      "\nYou can check for updates manually by looking at the latest release in the GitHub repository:"
                      "\nhttps://github.com/R1DF/Snakes-and-Ladders-Simulation-Engine\n")
                return

            # If the status code is OK, compare versions gathered from the request
            latest_version = latest_version.json()["slse"]
            if latest_version == version:
                util.cheer("You're on the latest version!")
                print("No updates needed.\n")
            else:
                util.notify("A new version was detected!\n")
                print(f"Latest version: {latest_version}"
                      f"\nInstalled version: {version}"
                      f"\nPlease install the release manually from the release section of the repository:"
                      f"\nhttps://github.com/R1DF/Snakes-and-Ladders-Simulation-Engine\n")

        except Exception:
            # Mainly a catch-all to prevent Traceback messages for users
            util.alert("Failed to connect!"
                       "\nThis seems like a program issue or the game's versioning system was updated."
                       "\nPlease check out the repository of the game for any notices:"
                       "\nhttps://github.com/R1DF/Snakes-and-Ladders-Simulation-Engine\n")

