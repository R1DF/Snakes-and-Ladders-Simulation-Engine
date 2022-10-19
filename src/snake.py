# Imports
from sender import Sender

# Snake class
class Snake(Sender):
    def __init__(self, master, data):
        Sender.__init__(self, master, "LADDER", data)
        self.display_name = "SSS"