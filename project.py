import database
from datetime import datetime

def show_menu():
    print("\nBooks")
    print("1. Add a new book")
    print("2. Add a review")
    print("3. Show all books")
    print("4. Export books to CSV")
    print("5. Search books")
    print("6. Stop")

def add_book():
    title = input("Title of the book: ").strip()
    author = input("Author of the book: ").strip()
    purchase_date = input("Date when the book was purchased (YYYY-MM-DD): ").strip()
    
    try:
        datetime.strptime(purchase_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Use YYYY-MM-DD.")
        return

    status = input("Status of the book (Read/Unread): ").title()
    in_collection = input("Is the book in the collection? (yes/no): ").strip().lower() =="yes"

    database.add_book(title, author, purchase_date, status, in_collection)

def add_review():
    try:
        book_id = int(input("Enter the book ID: ").strip())
        rating = int(input("Rate the book (1 - 5): ").strip())
        if rating < 1 or rating > 5:
            print("Rating must be between 1 and 5!")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    finished_reading_date = input("Date when the book was finished (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(finished_reading_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Use YYYY-MM-DD.")
        return

    comments = input("Remarks about the book: ").strip()
    
    database.add_review(book_id, rating, finished_reading_date, comments)

def get_books():
    books = database.get_books()
    if books:
        print("\nBooks in the list: ")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Date of Purchase: {book[3]}, Status: {book[4]}, In Collection: {book[5]}")
    else:
        print("There are no books in the list.")

def search_books():
    query = input("Enter title or author to search: ").strip()
    books = database.search_books(query)
    if books:
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Date of Purchase: {book[3]}, Status: {book[4]}, In Collection: {book[5]}")
    else:
        print("No books found matching your search.")

def main():
    database.create_tables()
    while True:
        show_menu()
        choice = input("Choose option (1-6): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            add_review()
        elif choice == '3':
            get_books()
        elif choice == '4':
            database.export_books_to_csv()
        elif choice == '5':
            search_books()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
