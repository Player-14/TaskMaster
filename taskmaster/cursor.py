from definitions import *
import datetime
import json
import pyfiglet

class Cursor():
	def __init__(self, file, db = []):
		super().__init__()
		self.file = file
		ascii_banner = pyfiglet.figlet_format("TaskMaster")
		print("**************************************************\n" + ascii_banner + "*************************************************\nBy Patrick Agaba\n")
		self.db = []
		cur_book = str()
		self.main()

	def main(self):
		inp = input("Select an action: [a] create a book [b] delete a book [c] select a book [d] view agenda")

		if inp == "a":
			book_select = input("Book name:\t")
			self.create_book(book_select)
			cur_book = book_select
		elif inp == "b":
			book_select = input("Book name:\t")
			self.db.pop(self.db.index(book_select))
		elif inp == "c":
			book_select = input("Book name:\t")
			self.cur_book = book_select
	
	def create_book(self, book_name):
		self.db.append(book(book_name, str(datetime.datetime.now())))
		self.cur_book = book_name

	def create_note(self, title, timestamp, priority = "B" data = None):
		book_ = self.db[self.db.index(self.cur_book)]

		book_.append(note(self.cur_book.name, self.cur_book.timestamp, title, timestamp, data))

	def create_todo(self, title, state = 'todo', timestamp = datetime.datetime.now(), priority = "B" scheduled = None, deadline = None,  data = None):
		book_ = self.db[self.db.index(self.cur_book)]
		
		book_.append(todo(self.cur_book.name, self.cur_book.timestamp, title, state, timestamp, priority, scheduled, deadline, data))

Cursor("yo")