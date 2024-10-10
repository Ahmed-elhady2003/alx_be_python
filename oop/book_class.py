class Book:
    def __init__(self, title, author, year):
        """
        Initializes a Book instance with the title, author, and publication year.
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """
        Prints a message when the object is deleted.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """
        Returns a string representation of the Book instance.
        Example: "1984 by George Orwell, published in 1949"
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """
        Returns an official string representation that can recreate the Book instance.
        Example: "Book('1984', 'George Orwell', 1949)"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"