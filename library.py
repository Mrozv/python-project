from classes import Book

books = []

def load_sample_books():
    for i in range(1, 26):
        books.append(Book(i, f"Autor {i}", f"Tytuł {i}", 2000 + i % 20, 100 + i, 3))

def list_books():
    print("\n📚 Lista książek:")
    for book in books:
        print(f"{book.id}. \"{book.title}\" by {book.author} ({book.year}) - {book.pages} stron - Liczba egz.: {book.copies}")

def edit_book():
    if not books:
        print("📭 Brak książek do edycji.")
        return

    list_books()
    try:
        book_id = int(input("\nPodaj ID książki do edycji: "))
    except ValueError:
        print("❌ Błąd: ID musi być liczbą.")
        return

    book = next((b for b in books if b.id == book_id), None)
    if not book:
        print("❌ Nie znaleziono książki.")
        return

    print(f"\nEdytujesz: \"{book.title}\" by {book.author}")
    
    new_author = input(f"Nowy autor (Enter = bez zmian) [{book.author}]: ") or book.author
    new_title = input(f"Nowy tytuł (Enter = bez zmian) [{book.title}]: ") or book.title
    try:
        new_year = input(f"Nowy rok wydania (Enter = bez zmian) [{book.year}]: ")
        new_year = int(new_year) if new_year else book.year

        new_pages = input(f"Liczba stron (Enter = bez zmian) [{book.pages}]: ")
        new_pages = int(new_pages) if new_pages else book.pages

        new_copies = input(f"Liczba egzemplarzy (Enter = bez zmian) [{book.copies}]: ")
        new_copies = int(new_copies) if new_copies else book.copies

    except ValueError:
        print("❌ Błąd: rok, strony i egzemplarze muszą być liczbami.")
        return

    book.author = new_author
    book.title = new_title
    book.year = new_year
    book.pages = new_pages
    book.copies = new_copies

    print("✅ Książka została zaktualizowana.")

