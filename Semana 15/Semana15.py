
# Ejercicios de Algoritmos de Ordenamiento

# 1. Crea un `bubble_sort` por tu cuenta sin revisar el código de la lección.
# 2. Modifica el `bubble_sort` para que funcione de derecha a izquierda, 
# ordenando los números menores primero (como en la imagen de abajo).

def bubble_sort(list_to_sort):
    for out_index in reversed(range(0, len(list_to_sort)- 1)):
        has_made_changes = False
        
        for index in reversed(range(0, len(list_to_sort)- 1 - out_index)):
            current_element = list_to_sort[index]
            next_element = list_to_sort[index + 1]
            
            print(f"Round{out_index}, Iteracion {index} elemento acutal {current_element}, siguente elemento {next_element} ")
        
            if current_element > next_element:
                print("elemento mayor, cambiado de sitio")
                list_to_sort[index] = next_element
                list_to_sort[index +1] = current_element
                has_made_changes = True
                
        if not has_made_changes:
            return
    
    
my_test_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

bubble_sort(my_test_list)
print(my_test_list)

#Ejercicios de Análisis de Algoritmos

# 1. Analice el algoritmo de `bubble_sort` usando la Big O Notation.

def bubble_sort(list_to_sort):  # O(1)
    for out_index in reversed(range(0, len(list_to_sort)- 1)):  # O(n)
        has_made_changes = False  # O(1)
        
        for index in reversed(range(0, len(list_to_sort)- 1 - out_index)):  # O(n)
            current_element = list_to_sort[index]  # O(1)
            next_element = list_to_sort[index + 1]  # O(1)
            
            print(f"Round{out_index}, Iteracion {index} elemento acutal {current_element}, siguente elemento {next_element} ")  # O(1)
        
            if current_element > next_element:  # O(1)
                print("elemento mayor, cambiado de sitio")  # O(1)
                list_to_sort[index] = next_element  # O(1)
                list_to_sort[index +1] = current_element  # O(1)
                has_made_changes = True  # O(1)
                
        if not has_made_changes:  # O(1)
            return  # O(1)
    
    
my_test_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  # O(1)

bubble_sort(my_test_list)  # O(n^2) 
print(my_test_list)  # O(n)
        
# 2. Analice los siguientes algoritmos usando la Big O Notation:

# print_numbers_times_2

def print_numbers_times_2(numbers_list): # O(n) 
    for number in numbers_list: # O(n) 
        print(number * 2) # O(1) 

# check_if_lists_have_an_equal

def check_if_lists_have_an_equal(list_a, list_b): # O(log n)
        for element_b in list_b: # O(n) 
            if element_a == element_b: # O(1) 
                return True #  O(1) 

        return False #  O(1) 

# print_10_or_less_elements

def print_10_or_less_elements(list_to_print): #  O(1) 
    list_len = len(list_to_print) # O(n) 
    for index in range(min(list_len, 10)): # O(1) 
        print(list_to_print[index]) # O(1) 

# generate_list_trios      

def generate_list_trios(list_a, list_b, list_c): # O(log n)
    result_list = [] # O(1) 
    for element_a in list_a: # O(n)
        for element_b in list_b: # O(m) 
            for element_c in list_c: # O(n^3)
                result_list.append(f'{element_a} {element_b} {element_c}') # O(1) 

    return result_list # O(1) 