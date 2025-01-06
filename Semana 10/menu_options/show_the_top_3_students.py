import csv
from menu_options.add_student import students

def show_top_3_students(students):
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
        except (ValueError, KeyError):
            print(f"Error: Invalid or missing data for {student.get('name', 'Unknown')} {student.get('last_name', 'Unknown')}.")
            input("\nPress Enter to return to the main menu...")
            continue
        
        average = (grade_spanish + grade_english + grade_socials + grade_science) / 4
        
        student_name = f"{student.get('name', 'Unknown')} {student.get('last_name', 'Unknown')}"
        averages[student_name] = {'average': average}

    if not averages:
        print("No valid student data to display.")
        input("\nPress Enter to return to the main menu...")
        return

    top_3 = sorted(averages.items(), key=lambda x: x[1]['average'], reverse=True)[:3]

    print("\nTop 3 Students:")
    for name, data in top_3:
        print(f"{name}: {data['average']:.2f}")
    
    input("\nPress Enter to return to the main menu...")