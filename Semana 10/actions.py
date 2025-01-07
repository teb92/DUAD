import csv
students = []



def add_new_student():
    while True:
        name = input("Enter Name: ")
        last_name = input("Enter last name: ")
        section = input("Section: ")
        while True:
            try:
                grade_spanish = int(input("Introduce spanish grade: "))
                break
            except ValueError:
                print("Please introduce only numbers")
        while True:
            try:
                grade_english = float(input("Introduce english grade: "))
                break
            except ValueError:
                print("Please introduce only numbers")
        while True:
            try:
                grade_socials = float(input("Introduce socials grade: "))
                break
            except ValueError:
                print("Please introduce only numbers")
        while True:
            try:
                grade_science = float(input("Introduce science grade: "))
                break
            except ValueError:
                print("Please introduce only numbers")
                
        student_data = {
            'name': name,
            'last_name': last_name,
            'section': section,
            'grade_spanish': grade_spanish,
            'grade_english': grade_english,
            'grade_socials': grade_socials,
            'grade_science': grade_science,
        }
        
        

        students.append(student_data)
        print(f"Added Student: {name} {last_name}")

        
        while True:
            add_more = input("Would you like to add another student? (s/n): ").strip().lower()
            if add_more == 'n':
                return
            elif add_more == 's':
                print("Let's add a new student!")
                break 
            else:
                print("This is not a valid option, only select(s/n)")

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
    
