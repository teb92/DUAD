# Ejercicios
# Cree una clase de Circle con:
# Un atributo de radius (radio).
# Un método de get_area que retorne su área.
import math
class Circle():
    def __init__(self,radius ):
        self.radius = radius
    def get_area(self):
        circle_area = math.pi * (self.radius ** 2)
        print(f'The area of the circle is {circle_area}')
        
radius_request = int(input("Add the radius of the circle: "))
circle_area_1 = Circle(radius_request)
circle_area_1.get_area()


# Cree una clase de Bus con:
# Un atributo de max_passengers.
# Un método para agregar pasajeros uno por uno (que acepte una instancia de Person como parámetro). 
# Este solo debe agregar pasajeros si lleva menos de su máximo. 
# Sino, debe mostrar un mensaje de que el bus está lleno.
# Un método para bajar pasajeros uno por uno (en cualquier orden).

class Bus():
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.current_count = 0 
        
    def contador_de_pasajeros(self):
        while True:
            try:
                print("\nDesea entrar, salir o terminar el programa?")
                entrar_o_salir = int(input("Para entrar digite 1, para salir digite 2, para salir del programa digite 0: "))
                
                if entrar_o_salir == 1:
                    if self.current_count < self.max_passengers:
                        print("\nPuede abordar")
                        self.current_count += 1
                    else:
                        print("\nAutobús lleno")

                elif entrar_o_salir == 2:
                    if self.current_count > 0:
                        print("\nBajando")
                        self.current_count -= 1
                        print(f"Pasajeros actuales: {self.current_count}")
                    else:
                        print("Autobus vacio")
                elif entrar_o_salir == 0:  # Terminar el programa
                    print("\nSaliendo del programa...")
                    break
                
                else:
                    print("Por favor, ingresa solo 1, 2 o 0.")
                    
            except ValueError:
                print("Por favor, ingresa solo 1 o 2.")
                
cantidad_pasajeros = int(input("De cuantos pasajeron es el bus?: "))
my_bus = Bus(cantidad_pasajeros)
my_bus.contador_de_pasajeros()





# Duplique el proyecto Sistema de Control de Estudiantes y modifíquelo para 
# usar objetos para guardar la información de los estudiantes (creando una clase de Student).
# Hay que cambiar los estudiantes de diccionarios a objetos.
# Hay que convertir la data del csv de diccionario a objeto al importar.
# Hay que convertir los objetos a diccionario al exportar a csv.
# Hay que modificar el acceso a los keys para accesar a atributos.
# student[’Name’] → student.name
# Antes
# def create_student(students_list):
# 	name = input("Inserte su nombre: ")
# 	score = input("Inserte su nota: ")
# 	# (...)
# 	students_list.append({
# 		"name": name,
# 		"score": score,
# 		# (...)
# 	})
# ​
# Despues
# class Student():
# 	def __init__(self, name, score):
# 		self.name = name
# 		self.score = score
# 		# (...)

# def create_student(students_list):
# 	name = input("Inserte su nombre: ")
# 	score = input("Inserte su nota: ")
# 	# (...)
# 	students_list.append(
# 		Student(name, score)
# 	)
# ​

import json

class Student:
    total_averages = []
    for_top_3 = []
    def __init__(self, name, last_name, section, grades):
        self.name = name
        self.last_name = last_name
        self.section = section
        self.grades = grades
    def __str__(self):
        return f"{self.name} {self.last_name}, Section: {self.section}, Grades: {self.grades}"
    
    def to_dict(self):
            return {
                "name": self.name,
                "last_name": self.last_name,
                "section": self.section,
                "grades": self.grades
            }



    @staticmethod
    def add_new_student(students):
        while True:
            name = input("Enter Name: ")
            last_name = input("Enter last name: ")
            section = input("Section: ")
            while True:
                try:
                    grade_spanish = int(input("Introduce spanish grade: "))
                    if 0 <= grade_spanish <= 100:
                        break
                    else:
                        print("The number must be between 0 and 100. Please try again.")
                except ValueError:
                    print("Please introduce only numbers")
            while True:
                try:
                    grade_english = float(input("Introduce english grade: "))
                    if 0 <= grade_english <= 100:
                        break
                    else:
                        print("The number must be between 0 and 100. Please try again.")
                except ValueError:
                    print("Please introduce only numbers")
            while True:
                try:
                    grade_socials = float(input("Introduce socials grade: "))
                    if 0 <= grade_socials <= 100:
                        break
                    else:
                        print("The number must be between 0 and 100. Please try again.")
                except ValueError:
                    print("Please introduce only numbers")
            while True:
                try:
                    grade_science = float(input("Introduce science grade: "))
                    if 0 <= grade_science <= 100:
                        break
                    else:
                        print("The number must be between 0 and 100. Please try again.")
                except ValueError:
                    print("Please introduce only numbers")
                    
            new_student = Student(
                        name=name,
                        last_name=last_name,
                        section=section,
                        grades={
                            "grade_spanish": grade_spanish,
                            "grade_english": grade_english,
                            "grade_socials": grade_socials,
                            "grade_science": grade_science
                        }
                    )
            
            

            students.append(new_student)
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

    @staticmethod
    def show_all_average(students):
        for student in students:
            average = sum(student.grades.values()) / len(student.grades)
            Student.total_averages.append(average)
            
        if len(Student.total_averages) > 0:
            overall_average = sum(Student.total_averages) / len(Student.total_averages)
            print(f"Promedio general de los estudiantes: {overall_average:.2f}")
            print(Student.total_averages)
        else:
            print("\nNo se encontraron promedios válidos para calcular.")
    @staticmethod
    def show_top_3_students(students):
        
        for student in students:
                average = sum(student.grades.values()) / len(student.grades)
                Student.for_top_3.append({
                    "name" : f"{student.name} {student.last_name}",
                    "average" : average
                })
                
        if len(Student.for_top_3) > 0:
            sorted_students = sorted(Student.for_top_3, key=lambda x: x["average"], reverse=True)
            print("\nTop 3 estudiantes:")
            for i, student in enumerate(sorted_students[:3]):
                print(f"{i+1}. {student['name']} - Promedio: {student['average']:.2f}")
        else:
            print("\nNo se encontraron promedios válidos para calcular.")

    @staticmethod
    def read_json_file(students):
        nombre_archivo = input("Por favor, ingresa el nombre del archivo CSV (incluyendo la extensión '.json'): ")
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as file:
                data = json.load(file) 
            for student_data in data:
                student = Student(
                    name=student_data['name'],
                    last_name=student_data['last_name'],
                    section=student_data['section'],
                    grades=student_data['grades']
                )
                students.append(student)
                print(f"Added student: {student.name} {student.last_name}")
        
            input("\nPress Enter to continue...")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            input("\nPress Enter to return to main menu...")

    @staticmethod
    def export_students_to_dictionary(students):
        
    
        if not students:
            print("No students available to export.")
            input("\nPress Enter to return to the main menu...")
            return
        else:
            try:
                students_as_dicts = [student.to_dict() for student in students]
                def write_json_file(file_path, data):
                    with open(file_path, 'w', encoding='utf-8') as file:
                        json.dump(data, file, indent=4, ensure_ascii=False)

                write_json_file('student_list.json', students_as_dicts)

                print("Students data successfully exported to student_list.json")
                input("\nPress Enter to return to the main menu...")
            except Exception as e:
                print(f"An error occurred while exporting to JSON: {e}")
            
    @staticmethod        
    def read_students_from_variable(students):
        if not students:
            print("No students have been registered yet.")
            input("\nPress Enter to return to the main menu...")
            return
        for i, student in enumerate(students, start=1):
            print(f"Student {i}:")
            print(f"  Name: {student.name} {student.last_name}")
            print(f"  Section: {student.section}")
            print("  Grades:")
            print(f"    Spanish: {student.grades['grade_spanish']}")
            print(f"    English: {student.grades['grade_english']}")
            print(f"    Social Studies: {student.grades['grade_socials']}")
            print(f"    Science: {student.grades['grade_science']}")
            print("-" * 30)
        input("\nPress Enter to return to the main menu...")       
    @staticmethod           
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
                Student.add_new_student(students)
            elif menu_option == 2:
                Student.read_students_from_variable(students)
            elif menu_option == 3:
                Student.show_top_3_students(students)
            elif menu_option == 4:
                Student.show_all_average(students)
            elif menu_option == 5:
                Student.export_students_to_dictionary(students)
            elif menu_option == 6:
                Student.read_json_file(students)
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
    
students = [
    Student(
        name="John",
        last_name="Doe",
        section="A",
        grades={
            "grade_spanish": 90,
            "grade_english": 85,
            "grade_socials": 80,
            "grade_science": 95
        }
    ),
    Student(
        name="Jane",
        last_name="Smith",
        section="B",
        grades={
            "grade_spanish": 5,
            "grade_english": 92,
            "grade_socials": 5,
            "grade_science": 89
        }
    ),
    Student(
        name="Alice",
        last_name="Johnson",
        section="C",
        grades={
            "grade_spanish": 78,
            "grade_english": 88,
            "grade_socials": 72,
            "grade_science": 85
        }
    ),
    Student(
        name="Bob",
        last_name="Brown",
        section="A",
        grades={
            "grade_spanish": 95,
            "grade_english": 90,
            "grade_socials": 85,
            "grade_science": 93
        }
    ),
    Student(
        name="Charlie",
        last_name="Davis",
        section="B",
        grades={
            "grade_spanish": 60,
            "grade_english": 75,
            "grade_socials": 70,
            "grade_science": 80
        }
    )
]

while True:
    should_continue = Student.menu()
    if not should_continue:
        break

# Cree las siguientes clases:
# Head
# Torso
# Arm
# Hand
# Leg
# Feet
# Ahora cree una clase de Human y conecte todas las clases de manera lógica por medio de atributos.
# Por ejemplo (este código esta incompleto, pero describe la idea):
# class Torso:
# 	def __init__(self, head, right_arm, ...):
# 		self.head = head
# 		self.right_arm = right_arm
# 		...

# class Arm:
# 	def __init__(self, hand):
# 		self.hand = hand


# right_hand = Hand()
# right_arm = Arm(right_hand)
# torso = (head, right_arm)


class Head:
    pass

class Torso:
    def __init__(self, head, left_arm, right_arm, left_leg, right_leg):
        self.head = head
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.right_leg = right_leg
        
class Arm:
    def __init__(self, hand):
        self.hand = hand
class Hand:
    pass
class Leg:
    def __init__(self, foot):
        self.foot = foot
class Feet:
    pass

class Human:
    def __init__(self, head, torso, left_arm, right_arm, left_hand, right_hand, left_leg, right_leg, left_foot, right_foot):
        self.head = head
        self.torso = torso
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_hand = left_hand
        self.right_hand = right_hand
        self.left_leg = left_leg
        self.right_leg = right_leg
        self.left_foot = left_foot
        self.right_foot = right_foot

head = Head()

left_hand = Hand()
right_hand = Hand()

left_arm = Arm(left_hand)
right_arm = Arm(right_hand)

left_foot = Feet()
right_foot = Feet()

left_leg = Leg(left_foot)
right_leg = Leg(right_foot)

torso = Torso(head, left_arm, right_arm, left_leg, right_leg)

human = Human(head, torso, left_arm, right_arm, left_hand, right_hand, left_leg, right_leg, left_foot, right_foot)
