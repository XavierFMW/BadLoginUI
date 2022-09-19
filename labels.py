import tkinter as tk

DEFAULT_FONT = "Times New Roman"
DEFAULT_SIZE = 16
FONT_SIZE_DIFFERENCE = 6


class PromptLabel:

	def __init__(self, parent, text, font=DEFAULT_FONT, size=DEFAULT_SIZE):
		self.label = self.initialize_label(parent, text, font, size)

		
	def initialize_label(self, parent, text, font, size):
		label = tk.Label(parent, text=text, font=(font, size), fg="black")
		return label

	
	def display(self):
		self.label.pack()



class ErrorLabel:
	
	Y_PADDING = 5

	def __init__(self, parent, text, font=DEFAULT_FONT, size=(DEFAULT_SIZE - FONT_SIZE_DIFFERENCE)):
		self.label = self.initialize_label(parent, text, font, size)

		
	def initialize_label(self, parent, text, font, size):
		label = tk.Label(parent, text=text, font=(font, size), fg="red")
		return label
		
	
	def display(self):
		self.label.pack(pady=self.Y_PADDING)

