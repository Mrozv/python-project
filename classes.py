class Book:
    def __init__(self, id, author, title, year, pages, copies):
        self.id = id
        self.author = author
        self.title = title
        self.year = year
        self.pages = pages
        self.copies = copies

class Student:
    def __init__(self, id, name, borrowed_books=None):
        self.id = id
        self.name = name
        self.borrowed_books = borrowed_books or [] 

    def can_borrow(self):
        return len(self.borrowed_books) < 5

