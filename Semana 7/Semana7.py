# Cree una calculadora por linea de comando. Esta debe de tener un número actual, 
# y un menú para decidir qué operación hacer con otro número:
# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División
# 5. Borrar resultado
# Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, 
# restar, multiplicar, o dividir por el actual. 
# El resultado debe pasar a ser el nuevo numero actual.
# Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, 
# o si ingresa un número invalido a la hora de hacer la operación.

def suma(numero_base, num1):
    return numero_base + num1

def resta(numero_base, num1):
    return numero_base - num1

def multiplicar(numero_base, num1):
    return numero_base * num1

def dividir(numero_base, num1):
    if num1 == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return numero_base / num1

def calculadora():
    numero_base = 0
    
    print("""Bienvenido a la calculadora, puede utilizar los simbolos:
          + para sumar , 
          - para restar , 
          * para multiplicar,
          / para dividir
          escriba "borrar" para volver a 0
          Siempre estripe enter despues de introducir un numero o sumbolo""")
    while True:
        print(f"Resultado: {numero_base}")
        
        valid_operations = ["+", "-", "*", "/", "borrar", "salir"]
        operacion = input("Operacion a realizar: ")
        if operacion not in valid_operations:
                print("Operación no válida. Debes ingresar +, -, *, /, borrar o salir.")
                continue
        if operacion == "salir":
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break
        elif operacion == "borrar":
            numero_base = 0
            print("El resultado ha sido reiniciado a 0.")
            continue
        
        elif numero_base == 0:
            try:
                numero_base = float(input())
            except ValueError:
                print("Debe ingresar un numero para la operacion")
                continue
            operacion = operacion
            print(numero_base + " " +operacion)
            try:
                num1 = float(input())
            except ValueError:
                print("Debe ingresar un numero para la operacion")
                continue
        else:
            numero_base = numero_base
            operacion = operacion
            print(numero_base + " " +operacion)
            
            try:
                num1 = float(input())
            except ValueError:
                print("Debe ingresar un numero para la operacion")
                continue

        if operacion == "+":
                numero_base = suma(numero_base, num1)
        if operacion == "-":
                numero_base = resta(numero_base, num1)
        if operacion == "*":
                numero_base = multiplicar(numero_base, num1)
        if operacion == "/":
                numero_base = dividir(numero_base, num1)

calculadora()