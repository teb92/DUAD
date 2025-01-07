
# 💪🏽 **Ejercicios**

# 1. Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

def funcion_1():
    print("Soy funcion 1")
    funcion_2()
    
def funcion_2():
    print("Soy funcion 2")
    
funcion_1()
    

# 2. Experimente con el concepto de scope:
#     1. Intente accesar a una variable definida dentro de una función desde afuera.

soy_variable_de_afuera = 7

def funcion_ejercicio_2_1 ():
    print(f"Esta es una variable de afuera: {soy_variable_de_afuera}")
funcion_ejercicio_2_1 ()
    

#     2.  Intente accesar a una variable global desde una función y cambiar su valor.
def funcion_ejercicio_2_2 ():
    print(f"Esta es una variable de afuera con otro valor: {soy_variable_de_afuera-1}")
funcion_ejercicio_2_2()

# 3. Cree una función que retorne la suma de todos los números de una lista.
#     1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#     2. [4, 6, 2, 29] → 41

lista_ejercicio_3 = [4, 6, 2, 29]

def suma_de_la_lista():
    main=0
    for numero in lista_ejercicio_3:
        main += numero
    print(main)
suma_de_la_lista()

# 4. Cree una función que le de la vuelta a un string y lo retorne.
#     1. Esto ya lo hicimos en iterables.
#     2. “Hola mundo” → “odnum aloH”

def imprimir_vuelta():
    texto_a_imprimir = "Hola mundo"
    print(texto_a_imprimir)
    print(texto_a_imprimir[::-1])
imprimir_vuelta()

# 5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#     1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def suma_de_tipo_letra():
    texto_mayusculas = "I love Nación Sushi"
    mayusculas = sum(1 for char in texto_mayusculas if char.isupper())
    minusculas = sum(1 for char in texto_mayusculas if char.islower())
    print(f"""hay {mayusculas} mayusculas y {minusculas} minusculas en la horacion: "{texto_mayusculas}""""")
suma_de_tipo_letra()

# 6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#     1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#     2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”
string_con_lineas = "python-variable-funcion-computadora-monitor"
print(f"Lista original: {string_con_lineas}")
def reordenar():
    lista_de_palabras=[]
    nuevo_texto = string_con_lineas.replace("-"," ")
    palabras = nuevo_texto.split()
    for i in palabras:
        lista_de_palabras.append(i)
    print("Lapabras sin guion en una lista:")
    print(lista_de_palabras)
    print("Lapabras ordenadas alfabéticamente:")
    print(sorted(lista_de_palabras))
    new_list_in_order = sorted(lista_de_palabras)
    print("Lapabras ordenadas alfabéticamente y separdas con guion:")
    print('-'.join(new_list_in_order))
    
reordenar()


# 7. Cree una función que acepte una lista de números 
# y retorne una lista con los números primos de la misma.
#     1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#     2. Tip 1: Investigue la logica matematica para averiguar
# si un numero es primo, y conviertala a codigo. 
# No busque el codigo, eso no ayudaria.
#     3. *Tip 2: Aquí hay que hacer varias cosas 
# (recorrer la lista, revisar si cada numero es primo, 
# y agregarlo a otra lista). Así que lo mejor es agregar 
# **otra función** para revisar si el numero es primo o no.*

lista_ejercicio_7 = [1, 4, 6, 7, 13, 9, 67]
lista_primos = []

def es_primo():
    for numero_lista in lista_ejercicio_7:
        if numero_lista < 2:
            print(f"{numero_lista} no es primo")
        else:
            for i in range(2, numero_lista):  # Probar divisores desde 2 hasta numero - 1
                if numero_lista % i == 0:  # Si es divisible, no es primo
                    print(f"{numero_lista} no es primo")
            else:
                lista_primos.append(numero_lista)
    print(f"Lista de numeros primos: {lista_primos}")

es_primo()
