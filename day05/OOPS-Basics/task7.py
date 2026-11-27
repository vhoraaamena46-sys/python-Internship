class Library:
    def __init__(self):
       self.__books=[]
       
    def add_book(self,title):
        self.__books.append(title)
        
    def remove_book(self,title):
        self.__books.remove(title)
        
    def list_books(self):
        print(self.__books)             
        
        
l=Library()

l.add_book("Python")
l.add_book("Java")
l.add_book("C++")

l.list_books()

l.remove_book("C++")

l.list_books()