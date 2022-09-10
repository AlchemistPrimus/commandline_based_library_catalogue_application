import sys
from main_library import LibraryCatalogue
import re

class Menu:
    """Commandline interface for the library catalogue application.
    """
    
    def __init__(self):
        """Initializing the library catalogue program and defining the point of access for to interact with the application
        """
        self.catalogue=LibraryCatalogue()
        self.options={
            "1":self.add_book,
            "2":self.view_books,
            "3":self.search_book,
            "4":self.replace_book,
            "5":self.quit
        }
        
    def display_menu(self):
        """
        Display the menu of the application on the commandline
        """
        symb1=u'\u2796'*22
        symb2='='*15
        symb3=u'\u2744'*52
        menu_options=f"""   
{symb3}
    Knowledge Street library system admin
    {symb1}|
        {symb2} Menu {symb2}
    {symb1}
    1. |Add book to the system
    {symb1}
    2. |View Book
    {symb1}
    3. |Search Book
    {symb1}
    4. |Replace Book
    {symb1}
    5. |Quit
{symb3}
        """
        print(menu_options)                                     
    
    def run(self):
        """start the application.
        """
        while True:
            self.display_menu()
            choice=input("Enter option: ")
            action=self.options.get(choice)
            if action:
                action()
            else:
                print(f"Invalid choice! {choice}")
        
    def add_book(self):
        author=input("Name of the author: ")
        title=input("Title of the book: ")
        shelf=input("Specify the shelf: ")
        if re.search('[a-zA-Z0-9]', author and title):
            self.catalogue.add_book(author, title, shelf)
            print("Book added")
        else:
            symbol=u'\u274C'
            symb=u'\u2757'*2
            print(f"\n{symbol} Author name or title missing please try again{symb}")
    
    def search_book(self, books=None):
        book_name=input("Enter the book name or title:")
        if re.search('[a-zA-Z0-9]',book_name):
            for book in self.catalogue.search_book(book_name):
                bk=f"ISBN: {book.id}\nAuthor: {book.author}\nTitle: {book.title}"
                symb3=u'\u2744'*52
                print(bk)
                print(f"\n{symb3}")        
        else:
            print("Book not found")
    
    def view_books(self):
        if len(self.catalogue.items) !=0:
            for book in self.catalogue.items:
                bk=f"ISBN: {book.id}\nAuthor: {book.author}\nTitle: {book.title}"
                symb3=u'\u2744'*52
                print(bk)
                print(f"\n{symb3}")
        else:
            print("No book in the library")
            
    
    def replace_book(self):
        book_id=input("Enter the book id: ")
        title=input("Enter the book title: ")
        new_author=input("Enter new authors name:")
        if re.search('[a-zA-Z0-9]',book_id and title and new_author) or len(self.catalogue.items)==0:
            self.catalogue.replace_book(book_id, title, new_author)
            print(f"\nBook {book_id} successfully replaced")
            
        else:
            print("Not saved. one or more details missing")
            
    def quit(self):
        print("You exited from the system")
        sys.exit(0)
    
if __name__=="__main__":
    Menu().run()