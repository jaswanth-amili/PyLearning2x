# Method overriding

class Animal:
    def __init__(self):
        pass

    def sound(self):
        return "Animal sound"


class Dog(Animal):
    def __init__(self):
        pass

    def sound(self):

        # To access parent's function we use super()
        super().sound()
        return "Dog sound"

dog = Dog()

print(dog.sound())