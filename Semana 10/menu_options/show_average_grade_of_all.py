import csv
from menu_options.add_student import students

def show_all_average(students):
    if not students:
        print("No students have been registered yet.")
        input("\nPress Enter to return to the main menu...")
        return

    averages = {}
    for student in students:
        try:
            grade_spanish = float(student['grade_spanish'])
            grade_english = float(student['grade_english'])
            grade_socials = float(student['grade_socials'])
            grade_science = float(student['grade_science'])
        except (ValueError, KeyError) as e:
            print(f"Error: Invalid or missing data for {student.get('name', 'Unknown')} {student.get('last_name', 'Unknown')}.")
            input("\nPress Enter to return to the main menu...")
            continue
        
        average = (grade_spanish + grade_english + grade_socials + grade_science) / 4
        
        student_name = f"{student.get('name', 'Unknown')} {student.get('last_name', 'Unknown')}"
        averages[student_name] = {'average': average}
    
    
    for name, person in averages.items():
        print(f"{name}: {person['average']}")
    input("\nPress Enter to return to the main menu...")
