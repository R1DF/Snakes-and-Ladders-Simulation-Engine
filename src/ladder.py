# Imports
from sender import Sender

# Ladder class
class Ladder(Sender):
    def __init__(self, master, data):
        Sender.__init__(self, master, "LADDER", data)
        self.display_name_raw = "#" * self.master.master.master.string_representative_width
        self.display_name = self.display_name_raw
        self.destination_display_name = "H" * self.master.master.master.string_representative_width
