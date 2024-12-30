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

	cursor.execute('SELECT * FROM books WHERE title = ?', (title,))
	existing_book = cursor.fetchall()
	if existing_book:
		print(f"Book '{title}' is already in the list!")
	else:
		cursor.execute('''INSERT INTO books (title, author, purchase_date, status, in_collection)
							VALUES (?, ?, ?, ?, ?)''', (title, author, purchase_date, status, in_collection))

		conn.commit()
		print(f"Book '{title}' is added to the list!")

	conn.close()
	
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

	cursor.execute('SELECT * FROM books WHERE book_id = ?', (book_id))
	book = cursor.fetchone()
	if not book:
		print(f"Book with ID {book_id} does not exist!")
		conn.close()
		return

	cursor.execute('SELECT * FROM reviews WHERE book_id = ?', (book_id))
	existing_review = cursor.fetchone()
	if existing_review:
		print(f"Book with ID {book_id} has already been reviewed")
	elif rating < 1 or rating > 5:
		print("Rating must be between 1 and 5!")
	else:
		cursor.execute('''INSERT INTO reviews (book_id, rating, finished_reading_dated, comments)
							VALUES (?, ?, ?, ?, ?)''', (book_id, rating, finished_reading_dated, comments))

		conn.commit()
		print(f"Review for book with id '{book_id}' is added!")

	conn.close()