from library import load_sample_books, list_books
from students import add_student, list_students

def main():
    load_sample_books()

    while True:
        print("\n--- MENU GŁÓWNE ---")
        print("1. Wyświetl wszystkie książki")
        print("2. Dodaj studenta")
        print("3. Wyświetl studentów")
        print("4. Wyjście")
        choice = input("Wybierz opcję: ")

        if choice == "1":
            list_books()
        elif choice == "2":
            add_student()
        elif choice == "3":
            list_students()
        elif choice == "4":
            print("Do widzenia!")
            break
        else:
            print("❌ Nie ma takiej opcji. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
