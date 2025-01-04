# 4. Cree un programa que elimine todos los números impares de una lista.
#     1. Ejemplos:
#     2. `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]` → `[2, 4, 6, 8]`

my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_numeros_pares = []

for i in my_list2:
    if i % 2 != 0: 
        print(f"Numero {i} es un numero impar")
    else:
        lista_numeros_pares.append(i)
print(f"Nueva lista de numeros pares: {lista_numeros_pares}")

# 5.Cree un programa que le pida al usuario 10 números, 
# y al final le muestre todos los números que ingresó, 
# seguido del numero ingresado más alto.

lista_de_numeros=[]

times = 1

print('Necesitamos que introduzca 10 numeros')
while times <= 10:
    numero_para_lista = int(input(f'Introduzca el numero {times} de 10: ' ))
    lista_de_numeros.append(numero_para_lista)
    times +=1
print(lista_de_numeros)
print(f"El numero mayor es {max(lista_de_numeros)}")
