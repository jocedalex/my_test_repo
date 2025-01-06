#Ejercicio 1
# 1. string + string → "holahola"
# 2. string + int → TypeError: can only concatenate str (not "int") to str
# 3. int + string → TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 4. list + list → print([1,2,3]+[4,5,6]) = [1, 2, 3, 4, 5, 6]
# 5. string + list → TypeError: can only concatenate str (not "list") to str
# 6. float + int → print(4.5+3) = 7.5
# 7. bool + bool → print(True+False) # 1+0 = 1



#Ejercicio 2
name=input("Ingrese su nombre: ")
last_name=input("Ingrese su apellido: ")
age=int(input("Ingrese su edad: "))

if age<=1:
    print(f"{name} {last_name} es un bebe")
elif age>1 and age<=12:
    print(f"{name} {last_name} es un niño")
elif age>12 and age<=18:
    print(f"{name} {last_name} es un adolescente")
elif age>18 and age<=30:
    print(f"{name} {last_name} es un adulto joven")
elif age>40 and age<=65:
    print(f"{name} {last_name} es un adulto")
else:
    print(f"{name} {last_name} es un adulto mayor")

#Ejercicio 3
import random

secret_number=random.randint(1,10)
num=0
while num!=secret_number:
    num=int(input("Adivina el numero secreto: "))

print("Felicidades, adivinaste el numero secreto")

#Ejercicio 4
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))

max=num1

if num2>max:
    max=num2

if num3>max:
    max=num3

print(f"El numero mayor es: {max}")

#Ejercicio 5
notas=[]
cant_aprobadas=0
cant_reprobadas=0
prom_aprobadas=0
prom_reprobadas=0
n=int(input("Ingrese la cantidad de notas: "))

for i in range(n):
    nota=int(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)
    if nota<70:
        cant_reprobadas+=1
        prom_reprobadas+=nota
    else:
        cant_aprobadas+=1
        prom_aprobadas+=nota

prom_aprobadas=prom_aprobadas/cant_aprobadas
prom_reprobadas=prom_reprobadas/cant_reprobadas
promedio=sum(notas)/n

print(f"Promedio general: {promedio}")
print(f"Promedio de aprobados: {prom_aprobadas} con {cant_aprobadas} aprobados")
print(f"Promedio de reprobados: {prom_reprobadas} con {cant_reprobadas} reprobados")