from library import load_sample_books, list_books
from students import add_student, list_students, borrow_book

def main():
    load_sample_books()

    while True:
        print("\n--- MENU GŁÓWNE ---")
        print("1. Wyświetl wszystkie książki")
        print("2. Dodaj studenta")
        print("3. Wyświetl studentów")
        print("4. Wypożycz książkę")
        print("5. Wyjście")
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
            print("Do widzenia!")
            break
        else:
            print("❌ Nie ma takiej opcji. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
