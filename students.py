from classes import Student
from library import books, list_books
import json
import os
from datetime import datetime, timedelta

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
    list_students()
    try:
        student_id = int(input("\nPodaj ID studenta: "))
    except ValueError:
        print("❌ Błąd: ID musi być liczbą.")
        return

    student = next((s for s in students if s.id == student_id), None)
    if not student:
        print("❌ Student nie istnieje.")
        return

    list_books()
    try:
        book_id = int(input("Podaj ID książki do wypożyczenia: "))
    except ValueError:
        print("❌ Błąd: ID musi być liczbą.")
        return

    book = next((b for b in books if b.id == book_id), None)
    if not book or book.copies <= 0:
        print("❌ Książka niedostępna.")
        return

    # Sprawdź, czy student już ma tę książkę
    if any(b["book_id"] == book_id for b in student.borrowed_books):
        print("📛 Już wypożyczono tę książkę.")
        return

    borrowed_at = datetime.today()
    due_date = borrowed_at + timedelta(days=7)  # np. 7 dni na zwrot

    student.borrowed_books.append({
        "book_id": book_id,
        "borrowed_at": borrowed_at.strftime("%Y-%m-%d"),
        "due_date": due_date.strftime("%Y-%m-%d")
    })
    book.copies -= 1

    print(f"✅ Książka wypożyczona do: {due_date.strftime('%Y-%m-%d')}")


def show_statistics():
    print("\n📊 Statystyki biblioteki")

    most_active = max(students, key=lambda s: len(s.borrowed_books), default=None)
    if most_active:
        print(f"👤 Najwięcej wypożyczeń: {most_active.name} ({len(most_active.borrowed_books)} książek)")

    borrow_counts = {}
    for student in students:
        for borrowed in student.borrowed_books:
            book_id = borrowed["book_id"]
            borrow_counts[book_id] = borrow_counts.get(book_id, 0) + 1

    if borrow_counts:
        most_common_id = max(borrow_counts, key=borrow_counts.get)
        most_common_book = next((b for b in books if b.id == most_common_id), None)
        if most_common_book:
            print(f"📘 Najczęściej wypożyczana książka: \"{most_common_book.title}\" ({borrow_counts[most_common_id]} razy)")


def remind_returns():
    print("\n🔔 Przypomnienia o zwrotach książek:\n")
    today = datetime.today().date()
    found = False

    for student in students:
        for record in student.borrowed_books:
            due_date = datetime.strptime(record["due_date"], "%Y-%m-%d").date()
            days_left = (due_date - today).days
            book = next((b for b in books if b.id == record["book_id"]), None)
            if not book:
                continue

            if days_left < 0:
                print(f"❌ {student.name} spóźniony z oddaniem \"{book.title}\" ({abs(days_left)} dni po terminie).")
                found = True
            elif days_left <= 2:
                print(f"⚠️ {student.name} musi oddać \"{book.title}\" za {days_left} dni.")
                found = True

    if not found:
        print("✅ Brak zaległych lub nadchodzących terminów.")
