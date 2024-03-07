# Hierarchical inheritance

class Vehicle:
    def info(self):
        return "this is a vehicle"

    def registration(self):
        return "This is a vehicle's registration"


class Car(Vehicle):
    def info(self):
        return "This is a car"


class Bicycle(Vehicle):
    def info(self):
        return "This is a bicycle"


car = Car()
bicycle = Bicycle()

print(car.info())
print(car.registration())