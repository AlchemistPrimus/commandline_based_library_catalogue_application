import datetime

#Unique identifier for books
ISBN_ID=0

class Book:
    """Book object class
    """
    
    def __init__(self, author, title, shelf="not placed"):
        """Necessary details for the book

        Args:
            author (string): Name of the author of the book
            title (string): Title of the book
            shelf (str, optional): where the book is located in the library e.g the shelf. Defaults to "not placed".
        """
        self.author = author
        self.title = title
        self.shelf = shelf
        self.date_added = datetime.date.today()#timestamp to when the book is added
        global ISBN_ID
        ISBN_ID += 1
        self.id = ISBN_ID
    
    def match(self, filter):
        """finding the perfect match according to the filter string entered

        Args:
            filter (string): string to find its match

        Returns:
            bool: true if a match of the filter string is found, false otherwise.
        """
        return filter in self.author or filter in self.title
    
class LibraryCatalogue:
    """Library catalogue object representation class
    """
    
    def __init__(self):
        """List, representing library catalogue that stores the books instance objects representing library books stored in the library.
        """
        self.items = []
    
    def add_book(self, author, title, shelf="not placed"):
        """adding book to the library catalogue represented by list

        Args:
            author (string): name of the author of the book to be added in the catalogue
            title (string): title of the book
            shelf (str, optional): location of the book in the catalogue to help find the book faster. Defaults to "not placed".
        """
        self.items.append(Book(author, title, shelf))
        
    def _find_book(self, book_id, filter):
        """Searches for a book, the search is based on the filter string entered

        Args:
            book_id (int): identification number to uniquely identify a book
            filter (string): key word to use in search

        Returns:
            book object or bool: returns the book object if it is found or a false boolean value if the book item is not found
        """
        for item in self.items:
            if str(item.id) == str(book_id) or item.match(filter):
                return item
        return False
    
    def replace_book(self, book_id, filter, new_author):
        """replacing an item with another one

        Args:
            book_id (int): unique id to identify the book to replace
            filter (string): optional string to locate the item to replace
            new_author (string): the replacement, i.e the author of the new book
        """
        available_ids=(j.id for j in self.items)
        for i in available_ids:
            if book_id in available_ids:
                self._find_book(book_id, filter).author = new_author
                self._find_book(book_id, filter).title = filter
                break
            else:
                print('ID not found.')
                break
         
    def search_book(self, filter):
        """filter or search for a particular book or item in the catalogue

        Args:
            filter (string): string entered to be used as key word for performing search

        Returns:
            tuple: tuple of items found that match a particular rule or filter rule
        """
        return (book for book in self.items if book.match(filter))    