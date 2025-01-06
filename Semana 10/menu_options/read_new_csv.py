import csv
from menu_options.add_student import students
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

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


    