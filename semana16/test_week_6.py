from pytest import raises
from week_6 import sumatoria, revert,case_check, ordenar_palabras, filtrar_primos

#Ejercicio 3

def test_sumatoria_with_short_lists():
    #arrange
    la_lista = [4, 6, 2, 29]
    #act
    result = sumatoria(la_lista)
    #assert
    assert result == 41

def test_sumatoria_with_long_lists():
    #arrange
    la_lista = [item for item in range(150)]
    #act
    result = sumatoria(la_lista)
    #assert
    assert result == 11175

def test_sumatoria_with_empty_lists():
    #arrange
    la_lista = []
    #act
    result = sumatoria(la_lista)
    #assert
    assert result == 0

#Ejercicio 4

def test_revert_with_short_strings():
    #arrange
    my_string = 'Hello'
    #act
    result = revert(my_string)
    #assert
    assert result == 'olleH'

def test_revert_with_long_strings():
    #arrange
    my_string = 'Hello World'
    #act
    result = revert(my_string)
    #assert
    assert result == 'dlroW olleH'

def test_revert_with_non_string_elements():
    #arrange
    my_string = 90
    #act & assert
    with raises(TypeError):
        revert(my_string)


#Ejercicio 5

def test_case_check_with_short_strings():
    #arrange
    my_string = 'Hello World'
    #act
    result = case_check(my_string)
    #assert
    assert result == 'Uppercase: 2, Lowercase: 8'

def test_case_check_with_long_strings():
    #arrange
    my_string = 'Hello World, I am a Python Developer'
    #act
    result = case_check(my_string)
    #assert
    assert result == 'Uppercase: 5, Lowercase: 24'

def test_case_check_with_non_string_elements():
    #arrange
    my_string = 90
    #act & assert
    with raises(TypeError):
        case_check(my_string)

#Ejercicio 6

def test_ordenar_palabras_with_short_strings():
    #arrange
    palabras = 'python-variable-funcion-computadora-monitor'
    #act
    result = ordenar_palabras(palabras)
    #assert
    assert result == 'computadora-funcion-monitor-python-variable'

def test_ordenar_palabras_with_long_strings():
    #arrange
    palabras = 'python-variable-funcion-computadora-monitor-ram-rom'
    #act
    result = ordenar_palabras(palabras)
    #assert
    assert result == 'computadora-funcion-monitor-python-ram-rom-variable'

def test_ordenar_palabras_with_non_string_elements():
    #arrange
    palabras = 90
    #act & assert
    with raises(AttributeError):
        ordenar_palabras(palabras)


#Ejercicio 7

def test_filtrar_primos_with_short_lists():
    #arrange
    lista_numeros = [1, 4, 6, 7, 13, 9, 67]
    #act
    result = filtrar_primos(lista_numeros)
    #assert
    assert result == [7, 13, 67]

def test_filtrar_primos_with_long_lists():
    #arrange
    lista_numeros = [item for item in range(150)]
    #act
    result = filtrar_primos(lista_numeros)
    #assert
    assert result == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149]

def test_filtrar_primos_with_empty_lists():
    #arrange
    lista_numeros = []
    #act
    result = filtrar_primos(lista_numeros)
    #assert
    assert result == []