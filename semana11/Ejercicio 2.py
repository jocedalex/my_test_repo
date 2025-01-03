class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Bus:
    def __init__(self):
        self.passengers = []
        self.max_passengers = int(input('Enter the maximum number of passengers for this Bus: '))

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
        else:
            print('The bus is full, unable to add more passengers')

    def remove_passenger(self):
        name=input('Enter the name of the passenger you want to remove:')

        for passenger in self.passengers:
            if passenger.name.lower() == name.lower():
                self.passengers.remove(passenger)
                return
            
        print('That passenger is not in the bus')

first_user=Person('John', 25)
second_user=Person('Jane', 30)

new_bus=Bus()
new_bus.add_passenger(first_user)
new_bus.add_passenger(second_user)

new_bus.remove_passenger()