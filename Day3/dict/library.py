# You are building a Library Management System in Python. The system should store books in a dictionary where:
# Key → Book ID
# Value → Book Title
# Write a Python program to perform the following operations using Dictionaries:
# Add a book to the library (Book ID, Title).
# Remove a book using Book ID.
# Search for a book by Book ID and display the title.
# Update the title of a book (e.g., correction in title).
# Display all books in the library.
# Count the total number of books in the library.
# Check if a book title exists in the library (reverse lookup).

class Library:
    def __init__ (self):
        self.books = {}
    
    def add_book(self,book_id, title):
        if book_id in self.books:
            print(f"Book ID {book_id} already exists. Use update_book to change the title.")
        else:
            self.books[book_id] = title
            print(f"Book '{title}' added with ID {book_id}.")
    
    def remove_book(self, book_id):
        if book_id in self.books:
            removed_title = self.books.pop(book_id)
            print(f"Book '{removed_title}' with ID {book_id} removed.")
        else:
            print(f"Book ID {book_id} not found.")

    def search_book(self, book_id):
        if book_id in self.books:
            print(f"Book ID {book_id} found: '{self.books[book_id]}'.")
        else:
            print(f"Book ID {book_id} not found.")
    
    def update_book(self, book_id, new_title):
        if book_id in self.books:
            old_title = self.books[book_id]
            self.books[book_id] = new_title
            print(f"Book ID {book_id} updated from '{old_title}' to '{new_title}'.")
        else:
            print(f"Book ID {book_id} not found.")

    def display_books(self):
        if self.books:
            print("Books in the library:")
            for book_id, title in self.books.items():
                print(f"ID: {book_id}, Title: '{title}'")
        else:
            print("No books in the library.")
    
    def count_books(self):
        print(f"Total number of books in the library: {len(self.books)}")   

    def check_title_exists(self, title):
        if title in self.books.values():
            print(f"Book title '{title}' exists in the library.")
        else:
            print(f"Book title '{title}' does not exist in the library.")

# Example usage
library = Library()
data = {
    101: "The Great Gatsby",
    102: "To Kill a Mockingbird",
    103: "1984",
    104: "Pride and Prejudice",
    105: "The Catcher in the Rye",
    106: "The Lord of the Rings",
    107: "Harry Potter and the Sorcerer's Stone",
    108: "The Hobbit",
    109: "Moby Dick",
    110: "War and Peace"
}
for book_id, title in data.items():
    library.add_book(book_id, title)
library.display_books()
library.search_book(1)
library.update_book(2, "Nineteen Eighty-Four")