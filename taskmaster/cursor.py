from definitions import *
from operator import attrgetter
import datetime
import json
import pyfiglet

class Cursor():
	def __init__(self, file, db = []):
		super().__init__()
		self.file = file

		# print intro
		ascii_banner = pyfiglet.figlet_format("TaskMaster")
		print("**************************************************\n" + ascii_banner + "**************************************************\nBy Patrick Agaba\n")
		
		# create a "db", a list of classes from definitions.py
		self.db = []

		# create string to store active book name
		self.cur_book = ""
		
		# run main
		self.main()

	def main(self):
		while True:
			if self.cur_book != "":
				book_action = input("\nBook:\t" + str(self.cur_book) + "\nBook actions:\n[a] create todo\n[b] create note\n[c] list notes\n[d] list todos\n[e] list pending todos\n")
				book_action = book_action.lower()

				if book_action == "a":
					todo_title = input("Name:\t")
					todo_state = input("State (press enter for default):\t")
					todo_priority = input("Priority (press enter for default):\t")
					todo_scheduled = input("Scheduled time (press enter for default):\t")
					todo_deadline = input("Deadline (press enter for default):\t")
					todo_data = input("Description (press enter for default):\t")
					self.create_todo(todo_title, todo_state, todo_priority, todo_scheduled, todo_deadline, todo_data)
				elif book_action == "b":
					note_title = input("Name:\t")
					note_priority = input("Priority (press enter for default):\t")
					note_data = input("Description (press enter for default):\t")
					self.create_note(note_title, str(datetime.datetime.now()), note_priority, note_data)
				elif book_action == "c":
					self.sort_book_priority()

					for bk in self.db:
						if bk.name == self.cur_book:
							for obj in bk.objects:
								if obj.type == "note":
									print("="*50)
									print("Title:\t" + obj.title)
									print("Timestamp:\t" + obj.timestamp)
									print("Priority:\t" + obj.priority)
									print("Description:\t" + obj.data)
				elif book_action == "d":
					self.sort_book_priority()
					
					for bk in self.db:
						if bk.name == self.cur_book:
							for obj in bk.obj:
								if obj.type == "todo":
									print("="*50)
									print("Title:\t" + obj.title)
									print("State:\t" + obj.state)
									print("Timestamp:\t" + obj.timestamp)
									print("Priority:\t" + obj.priority)
									print("Scheduled time:\t" + obj.scheduled)
									print("Deadline:\t" + obj.deadline)
									print("Description:\t" + obj.data)
					
					
				elif book_action == "e":
					self.sort_book_priority()
					for bk in self.db:
						if bk.name == self.cur_book:
							for obj in bk:
								if obj.type == "todo":
									if obj.state != "done":
										print("="*50)
										print("Title:\t" + obj.title)
										print("State:\t" + obj.state)
										print("Timestamp:\t" + obj.timestamp)
										print("Priority:\t" + obj.priority)
										print("Scheduled time:\t" + obj.scheduled)
										print("Deadline:\t" + obj.deadline)
										print("Description:\t" + obj.data)
				else:
					self.cur_book = ""	
			else:
				inp = input("Select an action:\n[a] create a book\n[b] delete a book\n[c] select a book\n[d] view agenda\n")

				inp = inp.lower()
				if inp == "a":
					book_select = input("\nBook name:\t")
					self.create_book(book_select)
					# select active book to created book
					self.cur_book = book_select
				elif inp == "b":
					book_select = input("\nBook name:\t")
					self.db.pop(self.db.index(book_select))
				elif inp == "c":
					book_select = input("\nBook name:\t")
					# select active book to selected book
					self.cur_book = book_select
				# TODO create a list book function
				# TODO create an agenda view
	
	def create_book(self, book_name):
		self.db.append(book(book_name, str(datetime.datetime.now())))
		self.cur_book = book_name

	def create_note(self, title, timestamp = str(datetime.datetime.now()), priority = "B", data = ""):
		for obj in self.db:
			if obj.name == self.cur_book:
				obj.objects.append(note(obj.name, obj.timestamp, "note", title, timestamp, priority, data))

		self.sort_book_priority()

	def create_todo(self, title, state = 'todo', timestamp = str(datetime.datetime.now()), priority = "B", scheduled = "", deadline = "",  data = ""):
		for obj in self.db:
			if obj.name == self.cur_book:
				obj.objects.append(todo(obj.name, obj.timestamp, "todo", title, state, timestamp, priority, scheduled, deadline, data))
		
		self.sort_book_priority()

	def sort_book_priority(self):
		for obj in self.db:
			if obj.name == self.cur_book:
				obj.objects = sorted(obj.objects, key=attrgetter('priority'))

Cursor("yo")