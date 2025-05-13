class Book:
    def __init__(self, id, author, title, year, pages, copies):
        self.id = id
        self.author = author
        self.title = title
        self.year = year
        self.pages = pages
        self.copies = copies

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.borrowed_books = []  # lista książek wypożyczonych
