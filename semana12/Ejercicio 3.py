# Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.

class Flyable:
    def fly(self):
        return "I can fly!"

class Swimmable:
    def swim(self):
        return "I can swim!"

class Bird(Flyable):
    def __init__(self, name):
        self.name = name

class Fish(Swimmable):
    def __init__(self, name):
        self.name = name

class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name

# Example usage
duck = Duck("Donald")
print(f"{duck.name} says: {duck.fly()} and {duck.swim()}")