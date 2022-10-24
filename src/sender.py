class Sender:
    def __init__(self, master, sender_type, data):
        # Initialization
        self.master = master
        self.sender_type = sender_type
        self.data = data
        self.display_name = None

        self.transports_to = self.data["coords"][1]
        self.questions = self.data["questions"]


    def send(self):
        pass
