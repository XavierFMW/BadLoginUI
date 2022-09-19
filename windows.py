from tkinter import ttk
import tkinter as tk
import labels
import widgets


class LoginWindow:

	USERNAME_LABEL_MESSAGE = "Enter your username below."
	PASSWORD_LABEL_MESSAGE = "Enter your password below."
	ERROR_LABEL_MESSAGE = "Whoops! Look like that password was already taken by xX_beefcake_Xx!"

	USERNAME_LENGTH = 8
	PASSWORD_LENGTH = 10

	def __init__(self, title="Login Prompt", dimensions=None):
		self.window = self.__initialize_window(title, dimensions)
		self.username_frame, self.password_frame = self.__initialize_frames()
		self.__initialize_labels()
		self.__initialize_widgets()
		self.__initialize_buttons()

	
	def __initialize_window(self, title, dimensions):
		window = tk.Tk()
		window.title(title)

		if dimensions:
			window.geometry(dimensions)

		return window


	def __initialize_frames(self):
		
		username_frame = tk.Frame(self.window, relief=tk.RAISED)
		username_frame.pack()

		separator = ttk.Separator(self.window, orient="horizontal").pack(fill="x")

		password_frame = tk.Frame(self.window, relief=tk.RAISED)
		password_frame.pack()

		separator = ttk.Separator(self.window, orient="horizontal").pack(fill="x")

		return username_frame, password_frame

	
	def __initialize_labels(self):
		
		username_label = labels.PromptLabel(self.username_frame, self.USERNAME_LABEL_MESSAGE)
		username_label.display()

		password_label = labels.PromptLabel(self.password_frame, self.PASSWORD_LABEL_MESSAGE)
		password_label.display()


	def __initialize_widgets(self):

		username_widget = widgets.DropdownTextEntry(self.username_frame, self.USERNAME_LENGTH)
		username_widget.display()

		password_widget = widgets.DropdownTextEntry(self.password_frame, self.PASSWORD_LENGTH)
		password_widget.display()
		
	
	def __initialize_buttons(self):
		
		button = tk.Button(self.window, text="Submit", command=self.__show_error)
		button.pack(pady=10)


	def __show_error(self):
		
		error_label = labels.ErrorLabel(self.password_frame, self.ERROR_LABEL_MESSAGE)
		error_label.display()

	
	def launch(self):
		self.window.mainloop()

