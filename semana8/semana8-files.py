#Ejercicio 1

def reorganize(file_name):
    with open(file_name+".txt", 'r', encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            print(line)
        lines.sort()
    with open(file_name+"sorted.txt", 'w', encoding="utf-8") as file:
        for line in lines:
            file.write(line)

path=input("Ingrese el nombre del archivo: ")
reorganize(path)
