#Ejercicio 1
def ask_option():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Limpiar")
    print("6. Salir")
    return int(input("Ingrese la opcion: "))

def operation(current_number,option):
    if option == 1:
        current_number+=int(input("Ingrese el numero a sumar: "))
    elif option == 2:
        current_number-=int(input("Ingrese el numero a restar: "))
    elif option == 3:
        current_number*=int(input("Ingrese el numero a multiplicar: "))
    elif option == 4:
        current_number/=int(input("Ingrese el numero a dividir: "))
    elif option == 5:
        current_number=0
    return current_number

def calculator():
    current_number=0
    option=0
    while option != 6:
        try:
            option=ask_option()

            if option >= 1 and option <= 5:
                current_number=operation(current_number,option)
            elif option == 6:
                break
            else:
                print("Opcion invalida")

        except ValueError:
            print("Solo se permiten numeros")
        except ZeroDivisionError:
            print("No se puede dividir por 0")
        except:
            print("Ocurrio un error") 

    print("Hasta luego")

if __name__ == "__main__":
    calculator()
