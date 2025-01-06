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

