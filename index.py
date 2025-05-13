from library import load_sample_books, list_books

def main():
    load_sample_books()

    while True:
        print("\n--- MENU GŁÓWNE ---")
        print("1. Wyświetl wszystkie książki")
        print("2. Wyjście")
        choice = input("Wybierz opcję: ")

        if choice == "1":
            list_books()
        elif choice == "2":
            print("Do widzenia!")
            break
        else:
            print("Nie ma takiej opcji. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
