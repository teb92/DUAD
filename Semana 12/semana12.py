# 1. Cree una clase de `BankAccount` que:
#     1. Tenga un atributo de `balance`.
#     2. Tenga un método para ingresar dinero.
#     3. Tengo un método para retirar dinero.
    
#     Cree otra clase que herede de esta llamada `SavingsAccount` que:

#     1. Tenga un atributo de `min_balance` que se pueda asignar al crearla.
#     2. Arroje un error si se intenta retirar dinero y el `balance` está debajo del `min_balance`.

class BankAccount:
    def __init__(self):
        self.balance = 6000
    
    def deposito_dinero(self):
        while True:
            try:
                monto_a_depositar = int(input("Cuanto dinero quiere depositar?: ")) 
                if monto_a_depositar > 0:
                    self.balance += monto_a_depositar
                    print(f"Se han depositado {monto_a_depositar} unidades. Saldo actual: {self.balance}")
                    break
                else:
                    print("El monto a depositar debe ser mayor a 0.")
            except ValueError:
                print("Error: Debes ingresar un número válido.")
                
    def retiro_dinero(self):
        while True:
            try:
                monto_a_retirar = int(input("Cuanto dinero quiere retirar?: ")) 
                if monto_a_retirar > 0 and monto_a_retirar <= self.balance:
                    self.balance -= monto_a_retirar
                    print(f"Se han retirado {monto_a_retirar} unidades. Saldo actual: {self.balance}")
                    break
                elif monto_a_retirar > self.balance:
                    print(f"No hay suficiente dinero. Tu saldo actual es {self.balance}.")
                else:
                    print("El monto a retirar debe ser mayor a 0.")
            except ValueError:
                print("Error: Debes ingresar un número válido.")
                
class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.min_balance = 5000
    
    def retiro_dinero_savings(self):
        while True:
            try:
                monto_a_retirar = int(input("Cuanto dinero quiere retirar?: ")) 
                if monto_a_retirar > 0 and (self.balance - monto_a_retirar) >= self.min_balance:
                    self.balance -= monto_a_retirar
                    print(f"Se han retirado {monto_a_retirar} unidades. Saldo actual: {self.balance}")
                    break
                elif monto_a_retirar > 0 and (self.balance - monto_a_retirar) < self.min_balance:
                    print(f"No hay suficiente dinero. Tu saldo actual es {self.balance}. Solo puedes retirar {(self.balance - self.min_balance)}")
                else:
                    print("El monto a retirar debe ser mayor a 0.")
            except ValueError:
                print("Error: Debes ingresar un número válido.") 




# 2. Cree una clase abstracta de `Shape` que:
#     1. Tenga los métodos abstractos de `calculate_perimeter` y `calculate_area`.
#     2. Ahora cree las siguientes clases que hereden de `Shape` 
#  e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
#     3. Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return self.side ** 2
    
    def calculate_perimeter(self):
        return 4 * self.side

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    
    

# 3. Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.

class Humano:
    def __init__(self, nombre, altura, edad):
        self.nombre = nombre
        self.altura = altura  # en metros
        self.edad = edad 
        
class Hombre(Humano):
    def __init__(self, nombre, altura, edad):
        super().__init__(nombre, altura, edad)
    def detalle_genero(self):
        print (f"Hola, me llamo {self.nombre}, mido {self.altura} metros y tengo {self.edad} años.")
        print("Soy Hombre")
class Mujer(Humano):
    def __init__(self, nombre, altura, edad):
        super().__init__(nombre, altura, edad)
    def detalle_genero(self):
        print (f"Hola, me llamo {self.nombre}, mido {self.altura} metros y tengo {self.edad} años.")
        print("Soy Mujer") 
    
hombre = Hombre("Carlos", 2.00, 34)
mujer = Mujer("Laura", 1.65, 30)

hombre.detalle_genero()
mujer.detalle_genero()
    