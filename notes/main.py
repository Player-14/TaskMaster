from collections import OrderedDict
import datetime

# Book model class
class book:
    def __init__(self, name, timestamp):
        super().__init__()
        self.name = name
        self.timestamp = timestamp

class note(book):
    def __init__(self, title, timestamp, data):
        super().__init__()
        self.title = title
        self.timestamp = timestamp
        self.data = data