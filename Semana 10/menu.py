import csv

from data import read_csv_file, read_csv_file, export_students_to_csv
from actions import add_new_student, read_students_from_variable, show_all_average, show_top_3_students, students




def menu():
    try:
        print("Students Control System")
        print("1 - Add a Student")
        print("2 - Review registered students")
        print("3 - Show the top 3 students with the highest grade point averages.")
        print("4 - Show the average grade among the grades of all students")
        print("5 - Export information to a new CSV file")
        print("6 - Import information from from a previous CSV file")
        print("7 - Exit")
        
        menu_option = int(input("Select a menu option (1 to 7): "))
        if menu_option == 1:
            add_new_student()
        elif menu_option == 2:
            read_students_from_variable(students)
        elif menu_option == 3:
            show_top_3_students(students)
        elif menu_option == 4:
            show_all_average(students)
        elif menu_option == 5:
            export_students_to_csv(students)
        elif menu_option == 6:
            read_csv_file()
        elif menu_option == 7:
            print("Bye!")
            return False  
        else:
            print("Invalid option, select a number between 1 to 7")
            input("\nPress Enter to return to continue...")
    except ValueError:
        print("That is not a number! Please select a number between 1 to 7.")
        input("\nPress Enter to return to continue...")
    return True 

