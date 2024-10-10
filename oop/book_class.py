class Book:
    def _init_(self, title, author, year):
        """
        Initializes a Book instance with the title, author, and publication year.
        """
        self.title = title
        self.author = author
        self.year = year
    
    def _del_(self):
        """
        Prints a message when the object is deleted.
        """
        print(f"Deleting {self.title}")
    
    def _str_(self):
        """
        Returns a string representation of the Book instance.
        Example: "1984 by George Orwell, published in 1949"
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def _repr_(self):
        """
        Returns an official string representation that can recreate the Book instance.
        Example: "Book('1984', 'George Orwell', 1949)"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"