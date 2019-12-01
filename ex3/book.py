# coding: utf8
from books_list import *

class Book():
    """Classe definissant un livre par
    -son titre
    -la page de garde
    -liste des pages"""

    def __init__(self, title, pages):
        """Constructeur de livre"""
        self.title = title
        self.pages= pages
        self.current_page='page de garde'

    '''def show_information(self):
        text="------------------\n \
        title: {}\n \
        pages: {}\n \
        page actuelle: {}"
        print(text.format(self.title, self.pages, self.current_page))

for book in books_list:
    livre= Book(title=book[0],pages=book[1])
    #livre.show_information()'''
