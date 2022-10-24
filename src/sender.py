class Sender:
    def __init__(self, master, sender_type, data):
        # Initialization
        self.master = master
        self.sender_type = sender_type
        self.data = data
        self.display_name = None
        self.display_name_raw = None
        self.destination = self.data["coords"][1]
        self.questions = self.data["questions"]

    def send(self, player):
        player.coordinates = self.destination.copy()

    def set_colour(self, colour):
        match colour:
            case "RED":
                self.display_name = f"R#{self.display_name_raw}~|"
            case "BLUE":
                self.display_name = f"B#{self.display_name_raw}~|"
            case "YELLOW":
                self.display_name = f"Y#{self.display_name_raw}~|"
            case "CYAN":
                self.display_name = f"C#{self.display_name_raw}~|"
            case "MAGENTA":
                self.display_name = f"M#{self.display_name_raw}~|"
            case "WHITE":
                self.display_name = f"W#{self.display_name_raw}~|"
            case "GREEN":
                self.display_name = f"G#{self.display_name_raw}~|"
