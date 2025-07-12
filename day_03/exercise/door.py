class Door:
    def __init__(self, closed):
        self.closed = closed

    def open(self, new_value):
        self.closed = False

    def close(self):
        self.closed = True
