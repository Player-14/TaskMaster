from collections import OrderedDict
import datetime
import json

# Book model class
class book:
    def __init__(self, name, timestamp):
        super().__init__()
        self.name = name
        self.timestamp = timestamp
    
    # class to return JSON of note data
    def printJSON(self):
        construct = {"name": self.name, "timestamp": self.timestamp}
        construct = json.dumps(construct)
        return construct

# note model class
class note(book):
    def __init__(self, book_name, book_timestamp, title, timestamp, data):
        super().__init__(book_name, book_timestamp)
        self.title = title
        self.timestamp = timestamp
        self.data = data

    # class to return JSON of note data
    def printJSON(self):
        construct = {"title": self.title, "timestamp": self.timestamp, "data": self.data}
        construct = json.dumps(construct)
        return construct