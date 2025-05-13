from classes import Book
import json
import os

books = [] 

def load_sample_books():
    books.clear()
    try:
        with open('sample_books.json', 'r', encoding='utf-8') as f:
            sample_books = json.load(f)
            for i, b in enumerate(sample_books, 1):
                book = Book(i, b["author"], b["title"], b["year"], b["pages"], b["copies"])
                books.append(book)
            print("📚 Załadowano przykładowe książki z pliku.")
    except FileNotFoundError:
        print("❌ Plik 'sample_books.json' nie został znaleziony.")
    except json.JSONDecodeError:
        print("⚠️ Błąd w pliku JSON.")


def save_books():
    data = [vars(b) for b in books]
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_books():
    # Jeśli plik nie istnieje – załaduj przykładowe książki
    if not os.path.exists("books.json"):
        load_sample_books()
        save_books()
        return

    with open("books.json", "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            if not data:
                raise ValueError("Pusty plik")
        except (json.JSONDecodeError, ValueError):
            print("⚠️ Plik books.json uszkodzony lub pusty. Ładowanie przykładowych książek.")
            load_sample_books()
            save_books()
            return

    books.clear()
    for item in data:
        books.append(Book(**item))

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

from students import students  # potrzebne do sprawdzania wypożyczeń

def delete_book():
    if not books:
        print("📭 Brak książek do usunięcia.")
        return

    list_books()
    try:
        book_id = int(input("\nPodaj ID książki do usunięcia: "))
    except ValueError:
        print("❌ Błąd: ID musi być liczbą.")
        return

    book = next((b for b in books if b.id == book_id), None)
    if not book:
        print("❌ Nie znaleziono książki.")
        return

    # Sprawdź, czy książka jest wypożyczona przez jakiegoś studenta
    borrowed_by_any = any(book_id in s.borrowed_books for s in students)
    if borrowed_by_any:
        print("❌ Nie można usunąć książki – jest aktualnie wypożyczona.")
        return

    confirm = input(f"Na pewno chcesz usunąć \"{book.title}\"? (t/n): ").strip().lower()
    if confirm == 't':
        books.remove(book)
        print("✅ Książka została usunięta.")
    else:
        print("⛔ Usuwanie anulowane.")

def add_book():
    print("\n➕ Dodawanie nowej książki:")

    title = input("Tytuł: ").strip()
    if not title:
        print("❌ Tytuł nie może być pusty.")
        return

    author = input("Autor: ").strip()
    if not author:
        print("❌ Autor nie może być pusty.")
        return

    try:
        year = int(input("Rok wydania: "))
        pages = int(input("Liczba stron: "))
        copies = int(input("Liczba egzemplarzy: "))
    except ValueError:
        print("❌ Rok, liczba stron i egzemplarzy muszą być liczbami.")
        return

    book_id = books[-1].id + 1 if books else 1
    new_book = Book(book_id, author, title, year, pages, copies)
    books.append(new_book)

    print(f"✅ Dodano książkę: \"{title}\" (ID: {book_id})")

