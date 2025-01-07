import random

#1 string + string → ?
texo_1 = "esto es un string"
texo_2 = "esto es otro string"
print(texo_1+texo_2)
#2. string + int → ?
print(f"3 {texo_1}")
#3. int + string → ?
print(f" {texo_1} 3")
#4. list + list → ?
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print(lista1+lista2)
#5. string + list → ?
print(f"3 {lista1}")
#6. float + int → ?
print(3+5.6)
#7. bool + bool → ?
print(True +True)

#Cree un programa que le pida al usuario su 
# nombre, apellido, y edad, y 
# muestre si es un bebé, niño, preadolescente, adolescente, 
# adulto joven, adulto, o adulto mayor.#

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))

if edad <= 2:
    print("Bebé")
elif 3 <= edad <= 10:
    print("Niño")
elif 11 <= edad <= 12:
    print("Preadolescente")
elif 13 <= edad <= 18:
    print("Adolescente")
elif 19 <= edad <= 30:
    print("Adulto joven")
elif 31 <= edad <= 59:
    print("Adulto")
else:
    (print("Adulto mayor"))
    
    # 3. Cree un programa con un numero secreto del 1 al 10. 
    # El programa no debe cerrarse hasta que el usuario adivine el numero.
    # 1. Debe investigar cómo generar un número aleatorio 
    # distinto cada vez que se ejecute.
numero_secreto = random.randint(1, 10)
numero_por_usuario = int(input("Adivina el numero secreto, Cual numero crees que es: "))

while (numero_secreto != numero_por_usuario):   
        numero_por_usuario = int(input("Fallaste intenta de nuevo: "))
print("""
   ___      __   _          _                    __      
  / _ | ___/ /  (_) _  __  (_)  ___  ___ _  ___ / /_ ___ 
 / __ |/ _  /  / / | |/ / / /  / _ \/ _ `/ (_-</ __// -_)
/_/ |_|\_,_/  /_/  |___/ /_/  /_//_/\_,_/ /___/\__/ \__/ 
                                                         """)


print(""""_______""")

#Cree un programa que le pida tres números al usuario y muestre el mayor.
print("""
▗▖  ▗▖█  ▐▌▄▄▄▄  ▗▞▀▚▖ ▄▄▄ ▄▄▄      ▗▖  ▗▖▗▞▀▜▌▄   ▄  ▄▄▄   ▄▄▄ 
▐▛▚▖▐▌▀▄▄▞▘█ █ █ ▐▛▀▀▘█   █   █     ▐▛▚▞▜▌▝▚▄▟▌█   █ █   █ █    
▐▌ ▝▜▌     █   █ ▝▚▄▄▖█   ▀▄▄▄▀     ▐▌  ▐▌      ▀▀▀█ ▀▄▄▄▀ █    
▐▌  ▐▌                              ▐▌  ▐▌     ▄   █            
                                                ▀▀▀             """)
numero_1 = int(input("Ingrese el primer numero "))
numero_2 = int(input("Ingrese el segundo numero "))
numero_3 = int(input("Ingrese el tercer numero "))
numero_mayor = max(numero_1, numero_2, numero_3)
print(f"El numero mayor es {numero_mayor}")

# 5. Dada `n` cantidad de notas de un estudiante, calcular:
#     1. Cuantas notas tiene aprobadas (mayor a 70).
#     2. Cuantas notas tiene desaprobadas (menor a 70).
#     3. El promedio de todas.
#     4. El promedio de las aprobadas.
#     5. El promedio de las desaprobadas.

cantidad_total_notas = int(input("Cuantas notas va a agregar?: "))
nota_aprovada = 0
nota_no_aprovada = 0
suma_nota_aprovada = 0
suma_nota_no_aprovada = 0

contador_nota = 1



while (cantidad_total_notas != 0):
    nota_s = int(input(F"Inserte nota {contador_nota}: "))
    if (nota_s > 70):
        print("Aprovada")
        suma_nota_aprovada = suma_nota_aprovada + nota_s
        nota_aprovada +=1
    else:
        print("Reprovada")
        suma_nota_no_aprovada = suma_nota_no_aprovada + nota_s
        nota_no_aprovada +=1
    contador_nota +=1
    cantidad_total_notas = cantidad_total_notas - 1
    
promedio_suma_nota_aprovada = suma_nota_aprovada / nota_aprovada
promedio_suma_nota_no_aprovada = suma_nota_no_aprovada / nota_no_aprovada

total_notas = nota_aprovada + nota_no_aprovada 

promedio_total = (suma_nota_aprovada + suma_nota_no_aprovada) / total_notas

print(f"Promedio de todas las Aprovadas: + {promedio_suma_nota_aprovada}")
print(f"Promedio de todas las Reprovadas: + {promedio_suma_nota_no_aprovada}")
print(f"Promedio de todas las notas: + {promedio_total}")


##
