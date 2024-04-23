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

# Function to load books from a CSV file
def load_books(book_list, csv_path):
    """Loads book data from a CSV file."""
    books_loading = True
    while books_loading:
        try:
            with open(csv_path, 'r', newline='') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # Skip the header row
                loaded_books = 0  
                for row in csv_reader:
                    if len(row) == 5:  # Ensure each row has all necessary data
                        isbn, title, author, genre, available = row
                        genre = int(genre)  # Convert genre to integer
                        available = available.lower() == 'true'  # Convert availability to boolean
                        book_list.append(Book(isbn, title, author, genre, available))
                        loaded_books += 1                     
            print("Book catalog has been loaded.")
            return loaded_books  
        except FileNotFoundError:
            csv_path = input("File not found. Re-enter the path to the CSV data file: ")
            continue
        except Exception as e:
            print(f"Error occurred while loading books: {e}")
            return 0

def print_books(book_list):
    """Prints the details of books."""
    print("Print book catalog")
    print("ISBN".ljust(15), "Title".ljust(25), "Author".ljust(25), "Genre".ljust(20), "Availability".ljust(15))
    print("-" * 15, "-" * 25, "-" * 25, "-" * 20, "-" * 15)
    for books in book_list:
        genre_name = Book.genre_names.get(books.get_genre_code(), "Unknown Genre")
        print(books.isbn.ljust(15), books.title.ljust(25), books.author.ljust(25), genre_name.ljust(20), books.get_availability().ljust(15))

def print_menu(menu_heading, menu_options):
    """Prints the menu options."""
    print(menu_heading)
    print("=" * len(menu_heading))
    for key, value in menu_options.items():
        print(f"{key}: {value}")

    while True:
        user_input = input("Enter your selection: ")
        if user_input in menu_options:
            return user_input
        if user_input == '2130':
            return user_input
        else:
            print("Invalid option.") 
            if user_input in menu_options: 
                return user_input

# Add comments to the rest of the functions as needed

def search_books(book_list, search_string):
    """Searches for books based on the given search string."""
    search_result = []
    for book in book_list:
        if (search_string.lower() in book.get_isbn().lower() 
            or search_string.lower() in book.get_title().lower() 
            or search_string.lower() in book.get_author().lower() 
            or search_string.lower() in book.get_genre_name().lower()): 
            search_result.append(book)
    return search_result

def borrow_book(book_list):
    """Handles the borrowing process for a book from the library."""
    isbn = input("Enter the 13-Digit ISBN (format 999-9999999999): ")
    book_available = next((book for book in book_list if book.get_isbn().lower() == isbn.lower()), None)
    if book_available:
        if book_available.get_availability() == "Available":
            book_available.borrow_it()
            print(f"'{book_available.get_title()}' with ISBN {isbn} succesfully borrowed.")
        else:
            print(f"'{book_available.get_title()}' with ISBN {isbn} is not currently available.")
    else:
        print("No book found with that ISBN.")

def return_book(book_list):
    """Handles the return process for a borrowed book to the library."""
    isbn = input("Enter the 13-Digit ISBN (format 999-9999999999): ")
    book = next((book for book in book_list if book.get_isbn().lower() == isbn.lower()), None)
    if book:
        if book.get_availability() == "Borrowed":
            book.return_it()
            print(f"'{book.get_title()}' with ISBN {isbn} successfully returned.")
        else:
            print(f"'{book.get_title()}' with ISBN {isbn} is not currently borrowed.")
    else:
        print("No book found with that ISBN.")

def add_book(book_list):
    """Adds a new book to the library."""
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    title = input("Enter title: ")
    author = input("Enter author: ")

    genre_valid = False
    while not genre_valid:
        genre_name = input("Enter genre: ").title()
        genre_code = next((code for code, name in Book.genre_names.items() if name.lower() == genre_name.lower()), None)
        if genre_code is not None:
            genre_valid = True
        else:
            print(f"Invalid genre name. Valid genre choices are: {', '.join(Book.genre_names.values())}")
        
    new_book = Book(isbn, title, author, genre_code, True)
    book_list.append(Book(isbn, title, author, genre_code, True))
    with open( 'books.csv', 'a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([new_book.isbn, new_book.title, new_book.author, new_book.genre_code, new_book.available])  
    print(f"'{title}' with ISBN {isbn} successfully added.")

def find_book_by_isbn(book_list, isbn):
  """Finds a book in the library by its ISBN."""
  for i, book in enumerate(book_list):
    if book.get_isbn() == isbn:
      return i
  return -1

def remove_book(book_list):
    """Removes a book from the library."""
    isbn = input("Enter the 13-digit ISBN format (999-9999999999): ")

    index = find_book_by_isbn(book_list, isbn)
    if index != -1:
        removed_book = book_list.pop(index)
        print(f"Book with ISBN {isbn} titled '{removed_book.get_title()}' has been removed from the library.")
    else:
        print("No book found with that ISBN.")
        with open('books.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["ISBN", "Title", "Author", "Genre Code", "Available"])
            for book in book_list:
                csv_writer.writerow([book.isbn, book.title, book.author, book.genre_code, book.available])
    
