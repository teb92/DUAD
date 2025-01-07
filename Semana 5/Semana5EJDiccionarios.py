
# 💪🏽 **Ejercicios**

# 1. Cree un diccionario que guarde la siguiente información sobre un hotel:
#     - `nombre`
#     - `numero_de_estrellas`
#     - `habitaciones`
# - El value del key de `habitaciones` debe ser una lista, y cada habitación debe tener la siguiente información:
#     - `numero`
#     - `piso`
#     - `precio_por_noche`

hoteles = [
    {
        "nombre" : "Hotel 1",
        "numero_estrellas" : 5,
        "habitaciones" : [
            {
                        "numero" : 1,
                        "piso" : 1,
                        "precio_por_noche" : 200
            },
            {
                        "numero" : 2,
                        "piso" : 12,
                        "precio_por_noche" : 300
            },
                        ]
    },
    {
        "nombre" : "Hotel 2",
        "numero_estrellas" : 3,
        "habitaciones" : [
            {
                        "numero" : 1,
                        "piso" : 1,
                        "precio_por_noche" : 200
            },
            {
                        "numero" : 2,
                        "piso" : 12,
                        "precio_por_noche" : 300
            },
        ]
    }
]

print(hoteles)

list_a = ["first_name", "last_name", "role"]
index = 0
for info in list_a:
    info2 = input(f"Your {info}: ")
    






# 2. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
#     1. Ejemplos:
#     2. `list_a = [’first_name’, ‘last_name’, ‘role’]`
#     `list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]`
#     → `{’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}`
list_a = ["first_name", "last_name", "role"]
diccionario_empleados = {}

for info in list_a:
    diccionario_empleados[info] = input(f"Your {info}: ")
    
print(diccionario_empleados)

# 3. Cree un programa que use una lista para eliminar keys de un diccionario.
#     1. Ejemplos:
#     2. `list_of_keys = [’access_level’, ‘age’]`
#     `employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}`
#     → `{’name’: ‘John’, 'email’: ‘john@ecorp.com’}`


employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}
print(f"Informacion actual:{employee}")
info_a_eliminar = int(input(
"""Que informacion quiere eliminar?
        1- name
        2- email
        3- access_level
        4- age
escriba el numero del valor que queire: """))


if info_a_eliminar == 1:
        employee.pop("name")
elif info_a_eliminar == 2:
        employee.pop("email")
elif info_a_eliminar == 3:
        employee.pop("access_level")
elif info_a_eliminar == 4:
        employee.pop("age")
else:
        print("Opción inválida. No se eliminó ninguna información.")


print(employee)