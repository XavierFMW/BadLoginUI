import tkinter as tk

DEFAULT_FONT = "Times New Roman"
DEFAULT_SIZE = 16


class PromptLabel:

	def __init__(self, parent, text, font=DEFAULT_FONT, size=DEFAULT_SIZE):
		self.label = self.initialize_label(parent, text, font, size)

		
	def initialize_label(self, parent, text, font, size):
		label = tk.Label(parent, text=text, font=(font, size), fg="black")
		return label

	
	def display(self):
		self.label.pack()



class ErrorLabel:

	def __init__(self, parent, text, font=DEFAULT_FONT, size=(DEFAULT_SIZE - 4)):
		self.label = self.initialize_label(parent, text, font, size)

		
	def initialize_label(self, parent, text, font, size):
		label = tk.Label(parent, text=text, font=(font, size), fg="red")
		return label
		
	
	def display(self):
		self.label.pack()

