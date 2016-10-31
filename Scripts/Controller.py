import sqlite3 as sql

class DB_Connector:

	def __init__(self, *args, **kwargs):

		self.table_name = 'products'
		self.id_column  = 'id'
		self.column_2   = 'upc'
		self.column_3   = 'name'
		self.column_4   = 'image'
		self.some_upc = ""

	
	def fetch_product(self):

		conn = sql.connect(
			"/Users/kellenreason/Development/raspi-telxon/Databases/Product.db")

		c = conn.cursor()

		c.execute("SELECT * FROM {tn} WHERE {upc}={my_upc}".\
	        format(tn=self.table_name, cn=self.column_2, 
	        	upc=self.column_2, my_upc=self.some_upc))
		
		upc_exists = c.fetchone()

		return upc_exists