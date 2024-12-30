import database

def show_menu():
	print("\nBooks")
	print("1. Add a new book")
	print("2. Add a review")
	print("3. Show all books")
	print("4. Stop")

def add_book():
	title = input("Title of the book: ")
	author = input("Author of the book: ")
	purchase_date = input("Date when the book was purchased (YYYY-MM-DD): ")
	status = input("Status of the book (Read/Unread): ").title()
	in_collection = input("Is the book in the collection? (yes/no): ").lower() =="yes"

	database.add_book(title, author, purchase_date, status, in_collection)

def add_review():
    book_id = int(input("Enter the book ID: "))
    rating = int(input("Rate the book (1 - 5): "))
    finished_reading_date = input("Date when the book was finished (YYYY-MM-DD): ")
    comments = input("Remarks about the book: ")
    
    database.add_review(book_id, rating, finished_reading_date, comments)

def get_books():
    books = database.get_books()
    if books:
        print("\nBooks in the list: ")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Date of Purchase: {book[3]}, Status: {book[4]}, In Collection: {book[5]}")
    else:
        print("There are no books in the list.")

def main():
    database.create_tables()
    while True:
        show_menu()
        choice = input("Choose option (1-4): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            add_review()
        elif choice == '3':
            get_books()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
