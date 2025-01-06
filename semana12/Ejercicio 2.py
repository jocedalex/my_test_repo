# 2. Cree una clase abstracta de `Shape` que:
#     1. Tenga los métodos abstractos de `calculate_perimeter` y `calculate_area`.
#     2. Ahora cree las siguientes clases que hereden de `Shape` e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
#     3. Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.
from math import pi

class Shape:
    def __init__(self):
        pass

    def calculate_perimeter(self):
        pass

    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * pi * self.radius

    def calculate_area(self):
        return pi * self.radius ** 2
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return 4 * self.side

    def calculate_area(self):
        return self.side ** 2
    
class Rectangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.base + self.height)

    def calculate_area(self):
        return self.base * self.height
    
my_circle = Circle(5)
print(my_circle.calculate_perimeter())
print(my_circle.calculate_area())

my_square = Square(5)
print(my_square.calculate_perimeter())
print(my_square.calculate_area())

my_rectangle = Rectangle(5, 10)
print(my_rectangle.calculate_perimeter())
print(my_rectangle.calculate_area())