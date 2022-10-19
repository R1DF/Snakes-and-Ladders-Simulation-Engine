class Sender:
    def __init__(self, master, sender_type, data):
        # Initialization
        self.master = master
        self.sender_type = sender_type
        self.data = data
        self.display_name = None

        self.transports_to = self.data["coords"][1]
        self.question = self.data["question"]
        self.answers = self.data["answers"]


    def send(self):
        pass
