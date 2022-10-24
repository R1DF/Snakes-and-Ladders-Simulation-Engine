# Base import
import os
import json
from menu import BaseMenu
from time import sleep
from util import wait, title
from packs_detector import get_zipped

# Packs viewer class
class PacksViewer(BaseMenu):
    def __init__(self, master):
        BaseMenu.__init__(self, master)

    def load(self):
        title(f"Snakes and Ladders Engine v{self.master.version} - Pack Viewer")
        print("Loading packs...")
        sleep(self.master.config_loader.constants["RATE"])

        # Fetching all packs in the folder
        packs_zipped = get_zipped()
        if len(packs_zipped) == 0:
            print("You don't have any pack installed.\n")
            wait(True)
        else:
            print(f"\n{len(packs_zipped)} {'pack was' if len(packs_zipped) == 1 else 'packs were'} detected.")
            for file_index in range(len(packs_zipped)):
                pack_metadata = packs_zipped[file_index]
                pack_name = pack_metadata["name"]
                pack_author = pack_metadata["author"]
                pack_description = pack_metadata["description"]
                print(f"{file_index + 1}. {pack_name} (by {pack_author})\n{pack_description}\n\n")
            wait(True)

