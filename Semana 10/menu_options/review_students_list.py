import csv
from menu_options.add_student import students

def read_students_from_variable(students):
    if not students:
        print("No students have been registered yet.")
        input("\nPress Enter to return to the main menu...")
        return
    for i, student in enumerate(students, start=1):
        print(f"Student {i}:")
        print(f"  Name: {student['name']} {student['last_name']}")
        print(f"  Section: {student['section']}")
        print("  Grades:")
        print(f"    Spanish: {student['grade_spanish']}")
        print(f"    English: {student['grade_english']}")
        print(f"    Social Studies: {student['grade_socials']}")
        print(f"    Science: {student['grade_science']}")
        print("-" * 30)
    input("\nPress Enter to return to the main menu...")
    



