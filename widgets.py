import tkinter as tk


class DropdownTextEntry:

	CHARSET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$"
	Y_PADDING = 15

	def __init__(self, parent, length):
		self.frame = self.__initialize_frame(parent)
		self.__initialize_dropdowns(length)
	
	
	def __initialize_frame(self, parent):
		
		frame = tk.Frame(parent)
		return frame


	def __initialize_dropdowns(self, length):
		
		for n in range(length):	
			str_var = tk.StringVar()
			str_var.set(" ")
			dropdown = tk.OptionMenu(self.frame, str_var, *self.CHARSET)
			dropdown.grid(row=0, column=n)

	
	def display(self):
		self.frame.pack(pady=self.Y_PADDING)
		
