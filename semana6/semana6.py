# #Ejercicio 1

# def prin():
#     print("Welcome to my program")
#     bye()

# def bye():
#     print('Good Bye now!')

# prin()

#Ejercicio 2


globalvar = 50

def test_function():
    var1 = 10
    print(f'This is a test function {globalvar}') 
    #globalvar=100 ##UnboundLocalError: cannot access local variable 'globalvar' where it is not associated with a value
    #We can't change the value of a global variable inside a function without using the global keyword

#print(var1) #NameError: name 'var1' is not defined. Did you mean: 'vars'?
test_function()
print(globalvar) #50

#Ejercicio 3

def sumatoria(la_lista):
    suma = 0
    for item in la_lista:
        suma += item
    return suma

print(sumatoria([4, 6, 2, 29])) #41

#Ejercicio 4

def revert(my_string):
    new_string = ''
    for index in range(len(my_string),0,-1):
        new_string+=my_string[index-1]

    return new_string

print(revert('Hello')) #olleH

#Ejercicio 5

def case_check(my_string):
    upper = 0
    lower = 0
    for item in my_string:
        if item.isupper():
            upper+=1
        elif item.islower():
            lower+=1

    return f'Uppercase: {upper}, Lowercase: {lower}'

print(case_check('Hello World')) #Uppercase: 2, Lowercase: 8

#Ejercicio 6

def ordenar_palabras(palabras):
    lista_palabras = palabras.split('-')
    lista_palabras.sort()
    return '-'.join(lista_palabras)

print(ordenar_palabras('python-variable-funcion-computadora-monitor')) # computadora-funcion-monitor-python-variable

#Ejercicio 7
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def filtrar_primos(lista_numeros):
    return [num for num in lista_numeros if es_primo(num)]

print(filtrar_primos([1, 4, 6, 7, 13, 9, 67])) # [7, 13, 67]
