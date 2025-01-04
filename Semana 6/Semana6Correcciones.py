# Tu código del ejericio #3 está en el camino correcto, pero podemos mejorarlo. Considera estos puntos:
# • Nombres de variables: Utiliza nombres que describan claramente el propósito de la variable. En este caso, total sería más adecuado que main.
# • Retorno de la función: Una función debe devolver un resultado. Agrega return total para que la función devuelva la suma calculada.
# • Parámetro: Para hacer la función más flexible, pásale la lista de números como parámetro. Esto permitirá reutilizarla con diferentes listas.

lista_ejercicio_3 = [4, 6, 2, 29]

def suma_de_la_lista(lista):
        Total=0
        for numero in lista:
                Total += numero
        return Total

print(suma_de_la_lista(lista_ejercicio_3))

# Tu código del ejericio #4 está muy cerca de ser perfecto. Para completar la función de invertir una cadena, considera estos puntos:
# • Parámetro: Pasa la cadena que deseas invertir como argumento a la función.
# • Retorno: Utiliza return cadena[::-1] para devolver la cadena invertida de forma concisa.

texto_a_imprimir_ejemplo = "Hola mundo"

def imprimir_vuelta(texto_a_imprimir):
    texto_invertido = texto_a_imprimir[::-1]
    return texto_invertido

print(imprimir_vuelta(texto_a_imprimir_ejemplo))


# ¡Buen trabajo! Tu solución del ejercicio #6 está muy cerca. Para mejorarla, te sugiero:
# 1. Crear una función que tome la cadena como parámetro y retorne la cadena 
# ordenada. Esto hace tu código sea más reutilizable y legible.

string_con_lineas = "python-variable-funcion-computadora-monitor"
print(f"Lista original: {string_con_lineas}")

def reordenar(palabras_por_revisar):
    lista_de_palabras = palabras_por_revisar.split("-")
    new_list_in_order = sorted(lista_de_palabras)
    return str('-'.join(new_list_in_order))
    
resultado = reordenar(string_con_lineas)

print(f"Nueva lista ordenada: {resultado}")


# ejercicio #7  Función única: En lugar de crear una función para verificar si un número es primo, 
# estás realizando todo el proceso dentro de la función principal. Separar la lógica en funciones más pequeñas mejora la legibilidad y reutilización del código.
# • Impresiones dentro de la función: Es recomendable evitar imprimir dentro de las funciones, 
# ya que esto acopla el código a una salida específica. Lo ideal es que las funciones realicen cálculos y retornen resultados, y que las impresiones se hagan por separado.
# • Cálculo de números primos: Recomendamos validar el cálculo de números primos y 
# realizar pruebas para evaluar el resultado. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]

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
