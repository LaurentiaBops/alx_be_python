# System that tracks books in a library

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def is_checked_out(self):
        """Keeps track of the avaliabilty of books"""
        return self._is_checked_out

    def __str__(self):
        """Convert object to a string"""
        return f"{self.title} by {self.author}"

    def return_book(self):
        """Marks the book as returned/available"""
        return self._is_checked_out ==True
       
        


class Library(Book):
    def __init__(self):
        self._books = []
        self._checked_out_books = []
    
    
    def add_book(self,book):
        """Adds new books to the library system"""
        self._books.append(book)
    
    def check_out_book(self,title):
        """Checks out a book and marks it as unavaliable"""
        for book in self._books:
            if book.title == title:
                if book.is_checked_out:
                    book._is_checked_out = True
                    self._books.remove(book)
                    self._checked_out_books.append(book)
                    return
                else:
                    return
        
        

    
    def return_book(self,title):
        """Returning a book to the library system and making it avaliable again"""
        for book in self._checked_out_books:
            if book.title == title:
                book._is_checked_out = False
                self._books.append(book)
                self._checked_out_books.remove(book)
                return
                
            
            else:
                return


         

    def list_available_books(self):
        """Lists all avaliable books"""
        for book in self._books:
            print(f"-{book}")




     
        

