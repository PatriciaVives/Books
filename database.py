import sqlite3

def connect_to_db():
	conn = sqlite3.connect("books.db")
	return conn

def create_tables():
	conn = connect_to_db()
	cursor = conn.cursor()

#tabel books:
	cursor.execute('''CREATE TABLE IF NOT EXISTS books (
						book_id INTEGER PRIMARY KEY AUTOINCREMENT,
						title TEXT,
						author TEXT,
						purchase_date TEXT,
						status TEXT,
						in_collection BOOLEAN)'''
						)

#tabel reviews
	cursor.execute('''CREATE TABLE IF NOT EXISTS reviews (
						review_id INTEGER PRIMARY KEY AUTOINCREMENT,
						book_id INTEGER,
						rating INTEGER,
						finished_reading_date TEXT,
						comments TEXT,
						FOREIGN KEY (book_id) REFERENCES books (book_id))''')

	conn.commit()
	conn.close()