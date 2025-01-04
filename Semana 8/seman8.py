# Ejercicios de Manejo de Archivos

# Cree un programa que lea nombres de canciones de un archivo (línea por línea) y 
# guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def open_and_print_file(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        print("Contenido original del archivo:")
        for line in lines:
            print(line.strip()) 

def new_list_in_order(path,path2):
    with open(path, 'r') as file: 
        lines = file.readlines()
    sorted_lines = sorted(lines)

    print("\nLíneas ordenadas alfabéticamente:")
    for line in sorted_lines:
        print(line.strip()) 


    with open(path2, 'w') as file:
        file.writelines(sorted_lines)

open_and_print_file('hits_2024.txt')
new_list_in_order('hits_2024.txt',"hits_2024_sorted.txt" )

# Ejercicios de Manejo de CVS

# 1. Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.
#     1. Debe incluir:
#         1. Nombre
#         2. Género
#         3. Desarrollador
#         4. Clasificación ESRB

import csv


games_list = [
	{
		'Nombre': 'GTA',
		'Genero': 'Crimen',
		'Desarrollador': 'Loco Arts',
		'Clasificación_ESRB': 'M',
	},
	{
		'Nombre': 'WOW',
		'Genero': 'RPG',
		'Desarrollador': 'Loco Arts',
		'Clasificación_ESRB': 'T',
	},
    {
		'Nombre': 'Pajaron enojados',
		'Genero': 'Crimen',
		'Desarrollador': 'Loco Arts',
		'Clasificación_ESRB': 'E',
	},
    {
		'Nombre': 'Toys',
		'Genero': 'Crimen',
		'Desarrollador': 'Loco Arts',
		'Clasificación_ESRB': 'E',
	},
]

def write_csv_file(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)

write_csv_file('games.csv', games_list, games_list[0].keys())

# Lea sobre el resto de métodos del módulo csv aqui y cree una 
# version alternativa del ejercicio de arriba que guarde el 
# archivo separado por tabulaciones en vez de por comas.


games_list = [
	{
		'Nombre': 'GTA',
		'Genero': 'Crimen',
		'Desarrollador': 'Loco Arts',
		'Clasificación_ESRB': 'M',
	},
	{
		'Nombre': 'WOW',
		'Genero': 'RPG',
		'Desarrollador': 'Loco Arts',
		'Clasificación_ESRB': 'T',
	},
    {
		'Nombre': 'Pajaron enojados',
		'Genero': 'Crimen',
		'Desarrollador': 'Loco Arts',
		'Clasificación_ESRB': 'E',
	},
    {
		'Nombre': 'Toys',
		'Genero': 'Crimen',
		'Desarrollador': 'Loco Arts',
		'Clasificación_ESRB': 'E',
	},
]

def write_csv_file(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers, dialect='excel-tab')
        writer.writeheader()
        writer.writerows(data)

write_csv_file('games2.csv', games_list, games_list[0].keys())

# Ejercicios de Manejo de JSON

import json

#  Investigue cómo leer y escribir archivos `JSON` en Python
#  Cree un programa que permita agregar un Pokémon nuevo al archivo de arriba.
#     1. Debe leer el archivo para importar los Pokémones existentes.
#     2. Luego debe pedir la información del Pokémon a agregar.
#     3. Finalmente debe guardar el nuevo Pokémon en el archivo.

def leer_json_altual(path):
    with open(path, 'r', encoding='utf-8') as archivo:
            contenido = json.load(archivo)
            return contenido


def guardar_nuevo_pokemon(path, contenido):
    with open(path, 'w', encoding='utf-8') as archivo:
            json.dump(contenido, archivo, indent=4, ensure_ascii=False)
            print(f"Archivo JSON guardado en: {path}")
            
def datos_pokemon():
    nombre_ingles = input("Introduce el nombre en inglés del Pokémon: ")
    tipos = input("Introduce los tipos del Pokémon (separados por comas): ").split(',')
    hp = int(input("Introduce los puntos de vida (HP) del Pokémon: "))
    ataque = int(input("Introduce los puntos de ataque del Pokémon: "))
    defensa = int(input("Introduce los puntos de defensa del Pokémon: "))
    ataque_especial = int(input("Introduce los puntos de ataque especial del Pokémon: "))
    defensa_especial = int(input("Introduce los puntos de defensa especial del Pokémon: "))
    velocidad = int(input("Introduce los puntos de velocidad del Pokémon: "))

    nuevo_pokemon = {
        "name": {
            "english": nombre_ingles
        },
        "type": tipos,
        "base": {
            "HP": hp,
            "Attack": ataque,
            "Defense": defensa,
            "Sp. Attack": ataque_especial,
            "Sp. Defense": defensa_especial,
            "Speed": velocidad
        }
    }
    pokemones = leer_json_altual('pokemones.json')
    

    pokemones.append(nuevo_pokemon)

    guardar_nuevo_pokemon('pokemones.json', pokemones)

pokemones = leer_json_altual('pokemones.json')    
datos_pokemon()

