#Ejercicio 1

import csv

def create_csv(dict_data, filename):
    with open(filename+".csv", "w",encoding="utf-8",newline='') as file:
        writer = csv.DictWriter(file, fieldnames=dict_data[0].keys())
        writer.writeheader()
        writer.writerows(dict_data)

#Ejercicio 2
def create_csv2(dict_data, filename):
    with open(filename+"2.csv", "w",encoding="utf-8",newline='') as file:
        writer = csv.DictWriter(file, fieldnames=dict_data[0].keys(),delimiter='\t')
        writer.writeheader()
        writer.writerows(dict_data)

def main():
    while True:
        try:
            amount=int(input("Cuantos registros desea ingresar: "))
            data=[]
            for i in range(amount):
                data.append({'Nombre':input("Ingrese el nombre: "),
                        'Genero':input("Ingrese el genero: "),
                        'Desarrollador':input("Ingrese el desarrollador"),
                        'Clasificacion ESRB':input("Ingrese la clasificacion ESRB: ")})
            break
                
        except ValueError:
            print("Solo se permiten numeros")

        except:
            print("Ocurrio un error")

    create_csv(data, "videojuegos")
    create_csv2(data, "videojuegos")

if __name__ == '__main__':
    main()



