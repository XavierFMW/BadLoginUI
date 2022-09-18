import tkinter as tk
import labels


class LoginWindow:

	def __init__(self, title="Login Prompt", dimensions="500x500"):
		self.window = self.initialize_window(title, dimensions)
		self.initialize_labels()

	
	def initialize_window(self, title, dimensions):
		window = tk.Tk()
		window.title(title)
		window.geometry(dimensions)
		return window


	def initialize_labels(self):

		username_label = labels.PromptLabel(self.window, "Enter your username:")
		username_label.display()

		error_label = labels.ErrorLabel(self.window, "Whoops! Looks like an error ocurred.")
		error_label.display()

	
	def launch(self):
		self.window.mainloop()

