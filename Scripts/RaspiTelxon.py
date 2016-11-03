import tkinter as tk
import Controller as dbc
from PIL import Image, ImageTk

class RaspiTelxon(tk.Tk):
	
	def __init__(self, *args, **kwargs):
		
		tk.Tk.__init__(self, *args, **kwargs)
		
		container = tk.Frame(self)

		container.pack(side="top", fill="both", expand=True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.minsize(width=800, height=480)

		self.frames = {}
		self.result = ""

		for F in (StartPage, SearchPage, ResultsPage):

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont, *args):
		frame = self.frames[cont]
		frame.tkraise()
		
		if (args and (cont.__name__ == 'ResultsPage')):
			ResultsPage.display_results(self, args)

	def set_result(self, result):
		self.result = result

	def get_result(self):
		return self.result

class StartPage(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)

		label = tk.Label(self, text = "Start Page")
		label.pack(pady=10, padx=10)

		EnterAppButton = tk.Button(self, text="Start Using Raspi-Telxon!",
																command=lambda: controller.show_frame(SearchPage))
		EnterAppButton.pack()


class SearchPage(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)

		self.controller = controller

		UPC_Label = tk.Label(self, text="UPC")
		UPC_Label.pack()

		self.UPC_Entry = tk.Entry(self)
		self.UPC_Entry.pack()

		self.Search_Button = tk.Button(self, text="Search", 
															command=self.Search_Button_Get)
		self.Search_Button.pack()


	def Search_Button_Get(self):

		self.View_Result_Button = tk.Button(self, text="View Result", 
		command=lambda: self.controller.show_frame(ResultsPage, self.controller.get_result()))

		self.View_Result_Button.pack()
		upc = ""

		if(self.UPC_Entry.get() != ""):
			upc = self.UPC_Entry.get()

		database = dbc.DB_Connector()

		database.some_upc = upc

		result = database.fetch_product()
		
		self.controller.set_result(result)

		if(result is None):
			result_not_found = tk.Label(self, text="No Result Found!")
			result_not_found.pack()
			self.View_Result_Button.config(state='disabled')
		elif(result is not None):
			result_found_notification = tk.Label(self, text="Results Found!")
			result_found_notification.pack()
			self.View_Result_Button.config(state='normal')

class ResultsPage(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)

		self.controller = controller

		UPC_Label = tk.Label(self, text="Results Page!")
		UPC_Label.pack()


	def display_results(self, results):

		for result in results:
			(ID, UPC, name, imageURI) = result

		self.upc_label = tk.Label(self, text=UPC)
		self.upc_label.pack()

		self.name_label = tk.Label(self, text=name)
		self.name_label.pack()

		# load = Image.open(imageURI)
		# render = ImageTk.PhotoImage(load)
		# self.img_label = tk.Label(self, image=render)
		# self.img_label.image = render
		# self.img_label.place(x=0, y=0)

app = RaspiTelxon()
app.mainloop()