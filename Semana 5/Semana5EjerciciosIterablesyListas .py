# ; 1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
# ;     1. Ejemplos:
# ;     2. `first_list = [’Hay’, ‘en’, ‘que’, ‘iteracion’, ‘indices’, ‘muy’]`
# ;     `second_list = [’casos’, 'los’, ‘la’, ‘por’, ‘es’, ‘util’]` ->
# ;     Hay casos
# ;     en los
# ;     que la
# ;     iteracion por
# ;     indice es
# ;     muy util




first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']

for index in range(0, len(first_list)):
    print(f'{first_list[index]} {second_list[index]}')
    
# 2. Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
#     1. Pista: investigue de que otras maneras se puede usar el `range`.
#     2. Ejemplos:
#     3. `my_string = ‘Pizza con piña’` → 
#     a
#     ñ
#     i
#     p
    
#     n
#     o
#     c
    
#     a
#     z
#     z
#     i
#     p

my_string = 'Pizza con piña'

for char in my_string[::-1]:
	print(char)
 
print('Otra opcion')
 
my_string = 'Pizza con piña'

for character in range(len(my_string)-1, -1, -1):
	print(my_string[character])

# 3. Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
#     1. Ejemplos:
#     2. `my_list = [4, 3, 6, 1, 7]` → `[7, 3, 6, 1, 4]`

my_list1 = [4, 3, 6, 1, 7]
my_list1[0], my_list1[-1] = my_list1[-1], my_list1[0]
print(my_list1)

# 4. Cree un programa que elimine todos los números impares de una lista.
#     1. Ejemplos:
#     2. `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]` → `[2, 4, 6, 8]`

my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


for i in my_list2:
    if i % 2 != 0: 
        my_list2.remove(i)
    else:
        None
print(my_list2)
        

# Cree un programa que le pida al usuario 10 números, 
# y al final le muestre todos los números que ingresó, 
# seguido del numero ingresado más alto.

lista_de_numeros=[]

times = 1

print('Necesitamos que introduzca 10 numeros')
while times <= 10:
    numero_para_lista = input(f'Introduzca el numero {times} de 10: ' )
    lista_de_numeros.append(numero_para_lista)
    times +=1
print(lista_de_numeros)