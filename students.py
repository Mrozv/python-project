from classes import Student
from library import books
import json
import os

students = []

def save_students():
    data = []
    for s in students:
        data.append({
            "id": s.id,
            "name": s.name,
            "borrowed_books": s.borrowed_books
        })
    with open("students.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_students():
    if not os.path.exists("students.json"):
        return

    with open("students.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    students.clear()
    for item in data:
        s = Student(item["id"], item["name"])
        s.borrowed_books = item.get("borrowed_books", [])
        students.append(s)

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

def show_statistics():
    print("\n📊 Statystyki biblioteki")

    if not students:
        print("Brak studentów.")
        return

    top_student = max(students, key=lambda s: len(s.borrowed_books), default=None)

    if top_student and top_student.borrowed_books:
        print(f"👤 Najwięcej wypożyczeń: {top_student.name} ({len(top_student.borrowed_books)} książek)")
    else:
        print("👤 Brak wypożyczeń wśród studentów.")

    borrow_counts = {}

    for s in students:
        for book_id in s.borrowed_books:
            borrow_counts[book_id] = borrow_counts.get(book_id, 0) + 1

    if borrow_counts:
        most_borrowed_id = max(borrow_counts, key=borrow_counts.get)
        most_borrowed_book = next((b for b in books if b.id == most_borrowed_id), None)
        if most_borrowed_book:
            print(f"📚 Najczęściej wypożyczana książka: \"{most_borrowed_book.title}\" – {borrow_counts[most_borrowed_id]} razy")
    else:
        print("📚 Żadna książka nie została wypożyczona.")
