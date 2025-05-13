from classes import Book

books = []

def load_sample_books():
    for i in range(1, 26):
        books.append(Book(i, f"Autor {i}", f"Tytuł {i}", 2000 + i % 20, 100 + i, 3))

def list_books():
    print("\n📚 Lista książek:")
    for book in books:
        print(f"{book.id}. \"{book.title}\" by {book.author} ({book.year}) - {book.pages} stron - Liczba egz.: {book.copies}")
