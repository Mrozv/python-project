from classes import Student

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
