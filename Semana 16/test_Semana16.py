import pytest
from ejercicios_de_semana_6 import suma_de_la_lista, imprimir_vuelta, suma_de_tipo_letra, reordenar, encontrar_primos

# 💪🏽 **Ejercicios**

# 1. Cree los siguientes unit tests para el algoritmo `bubble_sort`:
#     1. Funciona con una lista pequeña.
#     2. Funciona con una lista grande (de más de 100 elementos.
#     3. Funciona con una lista vacía.
#     4. No funciona con parámetros que no sean una lista.

def bubble_sort(list_to_sort):
    for outer_index in range(len(list_to_sort) - 1):
        has_made_changes = False
        for index in range(len(list_to_sort) - 1 - outer_index):
            current_element = list_to_sort[index]
            next_element = list_to_sort[index + 1]
            print(f'-- Iteracion {outer_index}, {index}. Elemento actual: {current_element}, Siguiente elemento: {next_element}')
            if current_element > next_element:
                print('El elemento actual es mayor al siguiente. Intercambiándolos...')
                list_to_sort[index], list_to_sort[index + 1] = next_element, current_element
                has_made_changes = True
        if not has_made_changes:
            break  # Se usa break en lugar de return para asegurarse de que devuelva la lista
    
    return list_to_sort  # Ahora retorna la lista ordenada
        
def test_bubble_sort_works_with_small_list():
    list_input = [4,3,2]
    result = bubble_sort(list_input)
    assert result == [2, 3, 4]

def test_bubble_sort_works_with_big_list():
    list_input = [4, 3, 2, 7, 1, 9, 5, 12, 15, 8, 6, 20, 18, 11, 14, 10, 17, 19, 13, 16]
    result = bubble_sort(list_input)
    assert result == sorted(list_input) 

def test_bubble_sort_works_with_empty_list():
    list_input = []
    result = bubble_sort(list_input)
    assert result == []

def test_bubble_sort_not_a_list():
    with pytest.raises(TypeError): 
        bubble_sort(123) 


# 2. Cree unit tests para probar 3 casos de 
# éxito distintos de cada uno de los ejercicios de semana 6 
# (*exceptuando el 1 y 2*).

def test_suma_de_la_lista_short_list():
    list_input = [4,3,2]
    result = suma_de_la_lista(list_input)
    assert result == 9
    
def test_suma_de_la_lista_long_list():
    list_input = [4, 3, 2, 7, 1, 9, 5, 12, 15, 8, 6, 20, 18, 11, 14, 10, 17, 19, 13, 16]
    result = suma_de_la_lista(list_input)
    assert result == 210
    
def test_suma_de_la_lista_negative_value():
    list_input = [4,3,2,-5,-8]
    result = suma_de_la_lista(list_input)
    assert result == -4
    
###
def test_imprimir_vuelta_short_text():
    text_input = "Hello!"
    result = imprimir_vuelta(text_input)
    assert result == "!olleH"

def test_imprimir_vuelta_long_text():
    text_input = "My name is Esteban"
    result = imprimir_vuelta(text_input)
    assert result == "nabetsE si eman yM"

def test_imprimir_vuelta_empty():
    text_input = ""
    result = imprimir_vuelta(text_input)
    assert result == ""
    
#####

def test_suma_de_tipo_letra_mix():
    text_input = "I love Nación Sushi"
    mayusculas, minusculas = suma_de_tipo_letra(text_input)
    assert mayusculas == 3  
    assert minusculas == 13  

def test_suma_de_tipo_letra_only_uppercase():
    text_input = "HELLO WORLD"
    mayusculas, minusculas = suma_de_tipo_letra(text_input)
    assert mayusculas == 10 
    assert minusculas == 0  
    
def test_suma_de_tipo_letra_empty():
    text_input = ""
    mayusculas, minusculas = suma_de_tipo_letra(text_input)
    assert mayusculas == 0  
    assert minusculas == 0  

###
    
def test_reordenar_basic_text():
    text_input = "python-variable-funcion-computadora-monitor"
    result = reordenar(text_input)
    assert result == "computadora-funcion-monitor-python-variable"

def test_reordenar_empty_text():
    text_input = ""
    result = reordenar(text_input)
    assert result == ""

def test_reordenar_already_order():
    text_input = "computadora-funcion-monitor-python-variable"
    result = reordenar(text_input)
    assert result == "computadora-funcion-monitor-python-variable"
    
###

def test_encontrar_primos_short_list():
    list_input = [4,3,2]
    result = encontrar_primos(list_input)
    assert result == [3, 2]
    
def test_encontrar_primos_long_list():
    list_input = [4, 3, 2, 7, 1, 9, 5, 12, 15, 8, 6, 20, 18, 11, 14, 10, 17, 19, 13, 16]
    result = encontrar_primos(list_input)
    assert result == [3, 2, 7, 5, 11, 17, 19, 13]

def test_encontrar_empty_list():
    list_input = []
    result = encontrar_primos(list_input)
    assert result == []