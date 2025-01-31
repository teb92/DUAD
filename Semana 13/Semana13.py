
# 💪🏽 **Ejercicios**

# 1. Cree un decorador que haga print de los parámetros y retorno de la función que decore.

def print_info(funcion):
    def wrapper(x, y):
        print(f"Parameters to use: {x} y {y}")
        result = funcion(x, y)
        print(f"El result is: {result}")
        return result
    return wrapper

@print_info
def sum(a, b):
    return a + b

sum(3, 5)

# 2. Cree un decorador que se encargue de revisar si todos los parámetros de la 
# función que decore son números, y arroje una excepción de no ser así.

def validate_numbers(func):
    def wrapper(a, b):
        try:
            isinstance(a, (int, float)) and isinstance(b, (int, float))
            return func(a, b)
        except TypeError:
            return "Both arguments must be numbers"
    return wrapper

@validate_numbers
def sum(a, b):
    return a + b

print(sum(3, 5))  
print(sum(3, "five")) 

# 3. Cree una clase de `User` que:
#     - Tenga un atributo de `date_of_birth`.
#     - Tenga un property de `age`.
    
#     Luego cree un decorador para funciones que acepten un `User` como parámetro que se
# encargue de revisar si el `User` es mayor de edad y arroje una excepción de no ser así.

from datetime import date


class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )


def check_adult_user(func):
    def wrapper(*args, **kwargs):
        try:
            for arg in args:
                if isinstance(arg, User) and arg.age < 18:
                    raise Exception(f"User age {arg.age} is not an adult")
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
    return wrapper


@check_adult_user
def greet_user(user):
    print(f"Hello, User! You are {user.age} years old.")

adult_user = User(date(1990, 6, 15))
not_adult_user = User(date(2010, 1, 1))  

greet_user(adult_user) 
greet_user(not_adult_user)  
