# Imports
from sender import Sender

# Ladder class
class Ladder(Sender):
    def __init__(self, master, data):
        Sender.__init__(self, master, "LADDER", data)
        self.display_name = "#" * self.master.string_representative_width

