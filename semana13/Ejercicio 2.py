#Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.

def check_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("All arguments must be numbers")
        for arg in kwargs.values():
            if not isinstance(arg, (int, float)):
                raise TypeError("All arguments must be numbers")
        return func(*args, **kwargs)
    return wrapper

@check_numbers
def add(a, b):
    return a + b


add(1, 2)