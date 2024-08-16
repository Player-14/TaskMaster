from definitions import book, note, todo
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
			if self.cur_book != "": # Check to see if a book is selected
				
				book_action = input("\nBook:\t" + str(self.cur_book) + "\nBook actions:\n[a] create todo\n[b] create note\n[c] list notes\n[d] list todos\n[e] list pending todos\n")
				
				book_action = book_action.lower()
				
				# If action is to create a todo
				if book_action == "a":
					todo_title = input("Name:\t")
					todo_state = input("State (press enter for default):\t")
					todo_priority = input("Priority (press enter for default):\t")
					todo_scheduled = input("Scheduled time (press enter for default):\t")
					todo_deadline = input("Deadline (press enter for default):\t")
					todo_data = input("Description (press enter for default):\t")
					
					if todo_priority == "":
						todo_priority = "B"
					
					self.create_todo(todo_title, todo_state, todo_priority, todo_scheduled, todo_deadline, todo_data)
					
					# sort book based by priority
					self.sort_book_priority()
				
				# If action is to create a note
				elif book_action == "b":
					note_title = input("Name:\t")
					note_priority = input("Priority (press enter for default):\t")
					note_data = input("Description (press enter for default):\t")
					
					if note_priority == "":
						note_priority = "B"
					
					self.create_note(note_title, str(datetime.datetime.now()), note_priority, note_data)
					
					# sort book based by priority
					self.sort_book_priority()
				
				# If action is to list notes
				elif book_action == "c":
					# sort book based by priority
					self.sort_book_priority()

					for bk in self.db: #for all the books in db
						if bk.name == self.cur_book: #if book is the selected book
							for obj in bk.objects: #for all the objects in the selected book
								if obj.type == "note": #if the object is a note
									# print note data
									print("="*50)
									print("Title:\t" + obj.title)
									print("Timestamp:\t" + obj.timestamp)
									print("Priority:\t" + obj.priority)
									print("Description:\t" + obj.data)
				
				elif book_action == "d":
					# sort book based by priority
					self.sort_book_priority()
					
					for bk in self.db:
						if bk.name == self.cur_book:
							for obj in bk.objects:
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
					# sort book based by priority
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
				
				# if no option is selected, go to main screen
				else:
					self.cur_book = ""	
			else:
				inp = input("Select an action:\n[a] create a book\n[b] delete a book\n[c] select a book\n[d] list books\n[e] view agenda\n")

				inp = inp.lower()
				
				#if action is create a book
				if inp == "a":
					book_select = input("\nBook name:\t")
					self.create_book(book_select)
					
					# select active book to created book
					self.cur_book = book_select
				
				#if action is to delete a book
				elif inp == "b":
					book_select = input("\nBook name:\t")
					
					for bk in self.db:
						if bk.name == book_select:
							self.db.pop(self.db.index(bk))
					
				#if action is to select a book
				elif inp == "c":
					book_select = input("\nBook name:\t")
					
					for bk in self.db:
						if bk.name == book_select:
							# select active book to selected book
							self.cur_book = book_select
						else:
							assert BookDoesNotExistError
				
				#if action is to list all books
				elif inp == "d":
					for bk in self.db:
						print(bk.name)
				
					
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