class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Bus:
    def __init__(self,passengers):
        self.passengers = []
        self.max_passengers = passengers

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

try:
    passengers=int(input('Enter the maximum number of passengers for this Bus: '))
    new_bus=Bus(passengers)

except ValueError:
    print('Please enter a valid number for passangers limit')


option=0
while option !=3:
    try:
        option=int(input('Enter 1 to add a passenger or 2 to remove a passanger or 3 to continue: '))

        if option == 1:
            name=input('Enter the name of the passenger: ')
            age=int(input('Enter the age of the passenger: '))

            new_passenger=Person(name, age)
            new_bus.add_passenger(new_passenger)

        elif option == 2:
            new_bus.remove_passenger()

    except ValueError:
        print('Please enter a valid option')


