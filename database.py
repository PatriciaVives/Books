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

#functie toevoegen boek
def add_book(title, author, purchase_date, status, in_collection):
	conn = connect_to_db()
	cursor = conn.cursor()

	cursor.execute('''INSERT INTO books (title, author, purchase_date, status, in_collection)
						VALUES (?, ?, ?, ?, ?)''', (title, author, purchase_date, status, in_collection))

	conn.commit()
	conn.close()
	print(f"Book '{title}' is added!")

#functie opvragen boeken
def get_books():
	conn = connect_to_db()
	cursor = conn.cursor()

	cursor.execute('SELECT * FROM books')
	books = cursor.fetchall()

	conn.close()
	return books

#functie review toevoegen
def add_review(book_id, rating, finished_reading_dated, comments):
	conn = connect_to_db()
	cursor = conn.cursor()

	cursor.execute('''INSERT INTO reviews (book_id, rating, finished_reading_dated, comments)
						VALUES (?, ?, ?, ?, ?)''', (book_id, rating, finished_reading_dated, comments))

	conn.commit()
	conn.close()
	print(f"Review for book with id '{book_id}' is added!")