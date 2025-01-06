#Ejercicio 1
first_list = ['Hay','en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']

for index in range(len(first_list)):
    print(f"{first_list[index]} {second_list[index]}")

#Ejercicio 2
my_string = 'Pizza con piña'

for index in range(len(my_string),0,-1):
    print(my_string[index-1])

#Ejercicio 3

my_list = [4, 3, 6, 1, 7,8,9,10]

my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(my_list)

#Ejercicio 4
my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13]

for index in range(len(my_list2),0,-1):
    if my_list2[index-1] % 2 != 0:
        my_list2.pop(index-1)

print(my_list2)

#Ejercicio 5

new_list=[]
for index in range(10):
    new_list.append(int(input(f"Ingrese el numero {index+1}: ")))

print(new_list,f"El numero mayor es: {max(new_list)}")