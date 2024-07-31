from definitions import *
import datetime
import json
import pyfiglet

class Cursor():
	def __init__(self, file):
		super().__init__()
		self.file = file
		ascii_banner = pyfiglet.figlet_format("TaskMaster")
		print("**************************************************\n" + ascii_banner + "*************************************************\nBy Patrick Agaba\n")

	def main(self):
		pass

Cursor("yo")