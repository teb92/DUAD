

# 3. Cree una función que retorne la suma de todos los números de una lista.
#     1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#     2. [4, 6, 2, 29] → 41

lista_ejercicio_3 = [4, 6, 2, 29]

def suma_de_la_lista(lista):
        Total=0
        for numero in lista:
                Total += numero
        return Total

print(suma_de_la_lista(lista_ejercicio_3))

# 4. Cree una función que le de la vuelta a un string y lo retorne.
#     1. Esto ya lo hicimos en iterables.
#     2. “Hola mundo” → “odnum aloH”

texto_a_imprimir_ejemplo = "Hola mundo"

def imprimir_vuelta(texto_a_imprimir):
    texto_invertido = texto_a_imprimir[::-1]
    return texto_invertido

print(imprimir_vuelta(texto_a_imprimir_ejemplo))

# 5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#     1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def suma_de_tipo_letra(texto):
    # texto_mayusculas = "I love Nación Sushi"
    mayusculas = sum(1 for char in texto if char.isupper())
    minusculas = sum(1 for char in texto if char.islower())
    print(f"""hay {mayusculas} mayusculas y {minusculas} minusculas en la horacion: "{texto}""""")
    return mayusculas, minusculas
# suma_de_tipo_letra()

# 6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#     1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#     2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”
string_con_lineas = "python-variable-funcion-computadora-monitor"
print(f"Lista original: {string_con_lineas}")

def reordenar(palabras_por_revisar):
    lista_de_palabras = palabras_por_revisar.split("-")
    new_list_in_order = sorted(lista_de_palabras)
    return str('-'.join(new_list_in_order))
    
resultado = reordenar(string_con_lineas)

print(f"Nueva lista ordenada: {resultado}")


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


def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def encontrar_primos(lista):
        primos = []
        for numero in lista:
                if es_primo(numero):
                        primos.append(numero)
        return primos


resultado = encontrar_primos(lista_ejercicio_7)
print(resultado)
