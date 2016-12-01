import sqlite3 as sql

class DB_Connector:

	def __init__(self):

		self.dbStr = "/home/pi/dev/Databases/Products.db"
		self.table_name = 'products'
		self.id_column  = 'id'
		self.column_2   = 'upc'
		self.column_3   = 'name'
		self.column_4   = 'image'
		self.column_5   = 'uip'
		self.column_6   = 'unitSize'
		self.column_7   = 'ingredients'
		self.some_upc = ""
		self.result = ""

	
	def fetch_product(self):

		conn = sql.connect(self.dbStr)

		c = conn.cursor()

		my_upc = self.some_upc

		c.execute("SELECT * FROM products WHERE upc='%s'" % my_upc)
		
		result = c.fetchone()

		return result