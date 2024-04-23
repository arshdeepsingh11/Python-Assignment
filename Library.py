import csv

class Book:
    
    # Dictionary to map genre codes to genre names
    genre_names = {
        0: "Romance",
        1: "Mystery",
        2: "Science Fiction",
        3: "Thriller",
        4: "Young Adult",
        5: "Children's Fiction",
        6: "Self-help",
        7: "Fantasy",
        8: "Historical Fiction",
        9: "Poetry"
    }
    
    def __init__(self, isbn, title, author, genre_code, available):
        """Initializer of Book class which contains 5 attributes."""
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre_code = genre_code
        self.available = available
        
    # Getter methods for various attributes
    def get_genre_name(self):
        """Getter method to retrieve genre name"""
        return self.genre_names.get(self.genre_code, "Unknown Genre")

    def get_isbn(self):
        """Getter method to get the ISBN number of the book."""
        return self.isbn

    def get_title(self):
        """Getter method to get the title of the book."""
        return self.title

    def get_author(self):
        """Getter method to get the name of the author."""
        return self.author

    def get_genre_code(self):
        """Getter method to get the genre code."""
        return self.genre_code

    def get_availability(self):
        """Getter method to get the availability of the book."""
        return "Available" if self.available else "Borrowed"

    def borrow_it(self):
        """Set the availability to False when book is borrowed."""
        self.available = False

    def return_it(self):
        """Set the availability to True when book is returned."""
        self.available = True

    def __str__(self):
        """String method to display all the attributes."""
        return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Genre Code: {self.genre_code}, Available: {self.available}"

    
