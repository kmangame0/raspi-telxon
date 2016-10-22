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
 
	def searchButton(self):
		r = requests.post("http://bugs.python.org", data={'number': 12524, 'type': 'issue', 'action': 'show'})



root = tk()
root.mainloop()