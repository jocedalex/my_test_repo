# Cree un decorador que haga print de los parámetros y retorno de la función que decore.

def print_args_and_return(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}")
        print(f"Keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Return: {result}")
        return result
    return wrapper

@print_args_and_return
def add(a, b):
    return a + b


add(1, 2)