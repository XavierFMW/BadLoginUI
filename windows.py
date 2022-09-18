from tkinter import ttk
import tkinter as tk
import labels


class LoginWindow:

	def __init__(self, title="Login Prompt", dimensions="500x500"):
		self.window = self.initialize_window(title, dimensions)
		u, p = self.initialize_frames()
		self.username_frame = u
		self.password_frame = p

	
	def initialize_window(self, title, dimensions):
		window = tk.Tk()
		window.title(title)
		window.geometry(dimensions)
		return window


	def initialize_frames(self):
		
		username_frame = tk.Frame(self.window, relief=tk.RAISED)
		username_frame.pack()

		separator = ttk.Separator(self.window, orient="horizontal")
		separator.pack()

		password_frame = tk.Frame(self.window, relief=tk.RAISED)
		password_frame.pack()

		return username_frame, password_frame
		
	
	def launch(self):
		self.window.mainloop()

