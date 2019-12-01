from book import*
from library import *

class Reader():
    """contient le livre emprunte"""
    def __init__(self):
        self.book_borrowed = None

    def borrow_book(self, title, bib):
        """"""
        for elem in bib.library:
            if title == elem[0]:
                self.book_borrowed = bib.get_book(title, bib)
                return self.book_borrowed
            else:
                return "ce livre n existe pas dans la bibliotheque"

    def go_to_page(self, num_page):
        """"""
        if num_page in self.book.pages:
            self.book.current_page=num_page


    def next_page(self, num_page):
        """"""
        if num_page+1 in self.book.pages:
            self.book.current_page=num_page+1

    def previous_page(self, num_page):
        """"""
        if num_page>0:
            self.book.current_page=num_page-1

    def read(self):
        """"""
    print("contenu de la page {}".format(self.book.pages[self.book.current_page]))

    def read_book(self):
        """"""
        for i in self.book.pages:
            read(self)

'''bib=Library()
for book in books_list:
    #book = Book(title=book[0], pages=book[1])
    bib.add_book(book)
nour=Reader()
print(nour.borrow_book('La nuit des temps', bib))'''
