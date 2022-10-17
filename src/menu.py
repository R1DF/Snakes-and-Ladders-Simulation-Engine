# Imports
from util import clear

# Base class
class BaseMenu:
    def __init__(self, master):
        clear()
        self.master = master
        self.load()

    def load(self):
        pass  # Gets overridden

