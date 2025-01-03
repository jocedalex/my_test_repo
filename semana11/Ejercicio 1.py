from math import pi

class Circle:
    def __init__(self):
        self.radius = float(input("What's the radius for this new circle? "))

    def get_area(self):
        return pi * self.radius**2
    
new_circle = Circle()
print(f'The area of the circle is {new_circle.get_area()}')