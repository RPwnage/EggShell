class command:
    def __init__(self):
        self.name = "vibrate"
        self.description = "vibrate device"
        self.category = "misc"

    def run(self, session, cmd_data):
        session.send_command(cmd_data)
