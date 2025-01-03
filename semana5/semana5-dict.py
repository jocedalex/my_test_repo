#Ejercicio 1
hotel = {
    'nombre': 'Hotel Lifter',
    'numero_de_estrellas': 5,
    'habitaciones': [
        {'numero': 101, 'piso': 1, 'precio_por_noche': 150},
        {'numero': 102, 'piso': 1, 'precio_por_noche': 200},
        {'numero': 201, 'piso': 2, 'precio_por_noche': 250},
        {'numero': 202, 'piso': 2, 'precio_por_noche': 300}
    ]
}

print(hotel)

#Ejercicio 2
new_dict={}

list_a = ['first_name', 'last_name', 'role']
list_b = ['Joced', 'Nieves', 'Software Engineer']

for index in range(len(list_a)):
    new_dict[list_a[index]]=list_b[index]

print(new_dict)

#Ejercicio 3
list_of_keys = ['access_level', 'age']
employee = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}

for item in list_of_keys:
    employee.pop(item)

print(employee)