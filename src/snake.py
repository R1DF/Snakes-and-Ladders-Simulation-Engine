# Imports
from sender import Sender

# Snake class
class Snake(Sender):
    def __init__(self, master, data):
        Sender.__init__(self, master, "LADDER", data)
        self.display_name_raw = "S" * self.master.master.master.string_representative_width
        self.display_name = self.display_name_raw
        self.destination_display_name = "U" * self.master.master.master.string_representative_width

