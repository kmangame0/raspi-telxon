import tkinter as tk
import Controller as dbc
from PIL import Image, ImageTk
from tkinter import font

class RaspiTelxon(tk.Tk):
	
	def __init__(self):
		
		tk.Tk.__init__(self)

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.title("Raspi-Telxon")
		
		self.titleFont = font.Font(family='Helvetica', size=24)
		self.itemFont = font.Font(family='Helvetica', size=18)
		

		self.frames = {}
		self.result = ""
		self.container = container

		for F in (StartPage, SearchPage):

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

	# Just break out the for on line 23 into a function
	# Reduce duplicate code
	def custom_frame(self):
		result_frame = ResultsPage(self.container, self)
		self.frames[ResultsPage] = result_frame
		result_frame.grid(row=0, column=0, sticky="nsew")
		self.show_frame(ResultsPage)

	def set_result(self, result):
		self.result = result

	def get_result(self):
		return self.result


class StartPage(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)

		label = tk.Label(self, text = "Start Page", font=controller.titleFont)
		label.pack(pady=10, padx=10)

		EnterAppButton = tk.Button(self, text="Start Using Raspi-Telxon!", 
			font=controller.itemFont,command=lambda: controller.show_frame(SearchPage))

		EnterAppButton.pack()


class SearchPage(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)

		self.controller = controller

		UPC_Label = tk.Label(self, text="UPC", font=controller.titleFont)
		UPC_Label.pack()

		self.UPC_Entry = tk.Entry(self)
		self.UPC_Entry.pack()

		Search_Button = tk.Button(self, text="Search", 
															font=controller.itemFont, command=self.search)
		Search_Button.pack()


	def search(self):

		self.View_Result_Button = tk.Button(self, text="View Result", 
		font=self.controller.itemFont, command=lambda: self.controller.custom_frame())

		self.View_Result_Button.pack()
		
		upc = ""

		if(self.UPC_Entry.get() != ""):
			upc = self.UPC_Entry.get()

		database = dbc.DB_Connector()

		database.some_upc = upc

		result = database.fetch_product()
		
		self.controller.set_result(result)

		if(result is None):
			result_not_found = tk.Label(self, text="No Result Found!", font=self.controller.itemFont)
			result_not_found.pack()
			self.View_Result_Button.config(state='disabled')
		elif(result is not None):
			result_found_notification = tk.Label(self, text="Results Found!", font=self.controller.itemFont)
			result_found_notification.pack()
			self.View_Result_Button.config(state='normal')


class ResultsPage(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)

		(ID, UPC, name, imageURI) = controller.get_result()

		load = Image.open(imageURI)
		render = ImageTk.PhotoImage(load)
		
		img_label = tk.Label(self, image=render)
		img_label.image = render
		img_label.pack(side="left")

		name_label = tk.Label(self, text="Product: " + name, font=controller.titleFont)
		name_label.pack()

		upc_label = tk.Label(self, text="UPC: " + UPC, font=controller.itemFont)
		upc_label.pack()

app = RaspiTelxon()
app.geometry("800x480")
app.mainloop()