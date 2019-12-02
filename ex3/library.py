# coding: utf8
from book import *

class Library():
    """elle incremente la bibliotheque"""
    def __init__(self):
        self.library=[]

    def add_book(self, book):
        """Elle ajoute un livre a son catalogue"""
        self.library.append(book)

    def get_book(self, title):
        """elle renvoie l’objet livre correspondant sur la base d’un titre"""

        for elem in self.library:
            if title == elem[0]:
                print(elem)
                #return True
            #else:
                #return False


bib=Library()
for book in books_list:
    #book = Book(title=book[0], pages=book[1])
    bib.add_book(book)
print(bib.library)
bib.get_book('La légende de Gösta Berling')