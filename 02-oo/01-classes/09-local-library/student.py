class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for copy in self.books:
            if book.title == copy.title and book.author == copy.author:
                self.books.remove(copy)

    def search_books(self, search_string):
        books = []

        for copy in self.books:
            if search_string.lower() in copy.title.lower() or search_string.lower() in copy.author.lower():
                books.append(copy)

        return books