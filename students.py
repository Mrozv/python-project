from classes import Student
from library import books

students = []

def add_student():
    if len(students) >= 15:
        print("❌ Maksymalna liczba studentów (15) została osiągnięta.")
        return

    student_id = len(students) + 1
    name = input("Podaj imię i nazwisko studenta: ").strip()
    
    if not name:
        print("❌ Imię nie może być puste.")
        return

    students.append(Student(student_id, name))
    print(f"✅ Dodano studenta: {name} (ID: {student_id})")

def list_students():
    if not students:
        print("🔍 Brak studentów w systemie.")
    else:
        print("\n👥 Lista studentów:")
        for s in students:
            print(f"{s.id}. {s.name} – wypożyczone książki: {len(s.borrowed_books)}")

def borrow_book():
    if not students:
        print("❌ Brak studentów. Dodaj najpierw studenta.")
        return

    list_students()
    try:
        sid = int(input("Podaj ID studenta: "))
        student = next((s for s in students if s.id == sid), None)
        if not student:
            print("❌ Nie znaleziono studenta.")
            return
    except ValueError:
        print("❌ Błąd: ID musi być liczbą.")
        return

    if not student.can_borrow():
        print("❌ Ten student wypożyczył już 5 książek.")
        return

    from library import list_books
    list_books()
    try:
        bid = int(input("Podaj ID książki do wypożyczenia: "))
        book = next((b for b in books if b.id == bid), None)
        if not book:
            print("❌ Nie znaleziono książki.")
            return
    except ValueError:
        print("❌ Błąd: ID musi być liczbą.")
        return

    if book.copies <= 0:
        print("❌ Brak dostępnych egzemplarzy tej książki.")
        return

    student.borrowed_books.append(book.id)
    book.copies -= 1
    print(f"✅ {student.name} wypożyczył(a) \"{book.title}\".")