import json

# Book model class
class book:
    def __init__(self, name, timestamp):
        super().__init__()
        self.name = name
        self.timestamp = timestamp
        self.objects = []
    
    # class to return JSON of note data
    def printJSON(self):
        construct = {"name": self.name, "timestamp": self.timestamp}
        construct = json.dumps(construct)
        return construct

# note model class
class note(book):
    def __init__(self, book_name, book_timestamp, type, title, timestamp, priority, data):
        super().__init__(book_name, book_timestamp)
        self.type = type
        self.title = title
        self.timestamp = timestamp
        self.priority = priority
        self.data = data

    # class to return JSON of note data
    def printJSON(self):
        construct = {"note": {"title": self.title, "timestamp": self.timestamp, "data": self.data}}
        construct = json.dumps(construct)
        return construct

    def __repr__(self):
        return repr((self.title, self.timestamp, self.priority))

# todo model class
class todo(book):
    def __init__(self, book_name, book_timestamp, type, title, state, timestamp, priority, scheduled, deadline, data):
        super().__init__(book_name, book_timestamp)
        self.type = type
        self.title = title
        self.state = state
        self.timestamp = timestamp
        self.priority = priority
        self.scheduled = scheduled
        self.deadline = deadline
        self.data = data

    # class to return JSON of todo data
    def printJSON(self):
        construct = {"todo": {"title": self.title, "state": self.state, "timestamp": self.timestamp, "scheduled": self.scheduled, "deadline": self.deadline, "data": self.data}}
        construct = json.dumps(construct)
        return construct

    def __repr__(self):
        return repr((self.title, self.state, self.timestamp, self.priority, self.scheduled, self.deadline))