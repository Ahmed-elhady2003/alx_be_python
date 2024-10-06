class Book:
    def __init__(self, title, author):
        """Initialize a book with a title and author. It is available by default."""
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self.__is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available)."""
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self.__is_checked_out


class Library:
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []  # Private list to store books

    def add_book(self, book):
        """Add a new book to the library."""
        self.__books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title if it's available."""
        for book in self.__books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"Checked out '{book.title}'")
                    return
        print(f"Sorry, '{title}' is either not available or already checked out.")

    def return_book(self, title):
        """Return a book by its title if it's checked out."""
        for book in self.__books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f"Returned '{book.title}'")
                    return
        print(f"Sorry, '{title}' was not checked out or doesn't exist.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self.__books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available.")
