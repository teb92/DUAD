import csv

from actions import students
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

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
        
def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file) 
            for row in reader:
                student_data = {
                    'name': row['name'],
                    'last_name': row['last_name'],
                    'section': row['section'],
                    'grade_spanish': row['grade_spanish'],
                    'grade_english': row['grade_english'],
                    'grade_socials': row['grade_socials'],
                    'grade_science': row['grade_science'],
                }
                students.append(student_data)
                print(f"Added student: {student_data}")  
        input("\nPress Enter to return to continue...")  
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        input("\nPress Enter to return to continue...") 

def select_file():
    Tk().withdraw()
    file_path = askopenfilename(filetypes=[("CSV files", "*.csv")]) 
    if not file_path:
        messagebox.showinfo("No file selected", "No file was selected. Exiting the program.")
        return None
    return file_path



