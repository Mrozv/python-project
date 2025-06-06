from library import list_books, edit_book, delete_book, add_book
from students import add_student, list_students, borrow_book, show_statistics, students
from library import load_books, save_books, books
from students import load_students, save_students, remind_returns

def main():
    load_books()
    load_students()
    print(f"📘 Wczytano {len(books)} książek, 👤 {len(students)} studentów.")

    while True:
        print("\n--- MENU GŁÓWNE ---")
        print("1. Wyświetl wszystkie książki")
        print("2. Dodaj studenta")
        print("3. Wyświetl studentów")
        print("4. Wypożycz książkę")
        print("5. Dodaj książkę")
        print("6. Edytuj książkę")
        print("7. Usuń książkę")
        print("8. Statystyki biblioteki")
        print("9. Przypomnienia o zwrotach książek")
        print("10. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            list_books()
        elif choice == "2":
            add_student()
        elif choice == "3":
            list_students()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            add_book()
        elif choice == "6":
            edit_book()
        elif choice == "7":
            delete_book()
        elif choice == "8":
            show_statistics()
        elif choice == "9":
            remind_returns()
        elif choice == "10":
            save_books()
            save_students()
            print("✅ Dane zapisane. Do widzenia!")
            break
        else:
            print("❌ Nie ma takiej opcji. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
