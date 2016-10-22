from tkinter import *
from requests import *

class Telxon:

	def __init__(self, master):
		frame = Frame(master)
		frame.pack()

		UPC_Entry = Entry(master)
		UPC_Entry.pack(side=RIGHT)

		UPC_Label = Label(master, text="UPC")
		UPC_Label.pack(side=LEFT)

		self.searchButton = Button(frame, text="UPC Search", command=self.searchButton)
		self.searchButton.pack()

	def searchButton(self):
                print("Search button pressed")
        
root = Tk()
t = Telxon(root)
root.mainloop()
