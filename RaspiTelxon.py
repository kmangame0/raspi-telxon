from tkinter import *
import requests
import json

root = Tk()
root.resizable(width=False, height=False)
root.minsize(width=800, height=480)

def search_UPC():
	request = requests.get('https://api.upcitemdb.com/prod/trial/lookup?upc=611269546019')
	
	

UPC_Label = Label(root, text="UPC")
UPC_Entry = Entry(root)
Search_Button = Button(root, text="Search", command=search_UPC)

UPC_Label.grid(row=0)
UPC_Entry.grid(row=0, column=1)
Search_Button.grid(row=1, column=1)






#t = Telxon(root)
root.mainloop()