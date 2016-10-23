from tkinter import *
from requests import *

class Telxon:

	def __init__(self, master):
		frame = Frame(master)
		frame.pack()

		UPC_Label = (master, text="UPC")
		UPC_Entry = Entry(master)

		self.searchButton = Button(frame, text="UPC Search", command=self.searchButton)
		self.searchButton.pack(side=LEFT)

root = tk()
root.mainloop()