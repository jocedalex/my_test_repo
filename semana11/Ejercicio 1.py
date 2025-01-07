from math import pi

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius**2

try:    
    radius=float(input("What's the radius for this new circle? "))

    if radius < 0:
        raise ValueError

    new_circle = Circle(radius)
    print(f'The area of the circle is {new_circle.get_area()}')

except ValueError:
    print("Please enter a valid number major than 0")