#3. Cree un programa que use una lista para eliminar keys de un diccionario.
#     1. Ejemplos:
#     2. `list_of_keys = [’access_level’, ‘age’]`
#     `employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}`
#     → `{’name’: ‘John’, 'email’: ‘john@ecorp.com’}`

list_of_keys = ["access_level", "age"]
employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}
print(f"Informacion:{employee}")

for keys in list_of_keys:
    if keys in employee:
        employee.pop(keys)
        
print(f"Informacion actualizada:{employee}")