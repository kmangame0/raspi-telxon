import tkinter as tk
import Controller as dbc

class RaspiTelxon(tk.Tk):
	
	def __init__(self, *args, **kwargs):
		
		tk.Tk.__init__(self, *args, **kwargs)
		
		container = tk.Frame(self)

		container.pack(side="top", fill="both", expand=True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.minsize(width=800, height=480)

		self.frames = {}

		for F in (StartPage, SearchPage, ResultsPage):

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

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

		UPC_Label = tk.Label(self, text="UPC")
		UPC_Label.pack()

		self.UPC_Entry = tk.Entry(self)
		self.UPC_Entry.pack()

		self.Search_Button = tk.Button(self, text="Search", 
															command=self.Search_Button_Get)
		self.Search_Button.pack()
		#controller.show_frame(ResultsPage)
		
	def Search_Button_Get(self):
		upc = ""
		
		if(self.UPC_Entry.get() != ""):
			upc = self.UPC_Entry.get()

		database = dbc.DB_Connector(self)

		database.some_upc = upc

		result = database.fetch_product()

		print(result)

class ResultsPage(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)

		UPC_Label = tk.Label(self, text="Hello, World!")
		UPC_Label.pack()

app = RaspiTelxon()
app.mainloop()

		