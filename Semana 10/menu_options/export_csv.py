import csv

from menu_options.add_student import students

def export_students_to_csv(students):
    if not students:
        print("No students available to export.")
        input("\nPress Enter to return to the main menu...")
        return
    else:
        try:
            def write_csv_file(file_path, data, headers):
                with open(file_path, 'w', encoding='utf-8') as file:
                    writer = csv.DictWriter(file, headers)
                    writer.writeheader()
                    writer.writerows(data)
            write_csv_file('student_list.csv', students, students[0].keys())

            print("Students data successfully exported to student_list.csv")
            input("\nPress Enter to return to the main menu...")
        except Exception as e:
            print(f"An error occurred while exporting to CSV: {e}")
        




