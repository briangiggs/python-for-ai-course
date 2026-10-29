class Dog:
    def __init__(self,name, breed):
        self.name = name
        self.breed = breed

class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        return "Meow! Meow!"

liz = Cat(name ="Lizzy")

liz.name
liz.meow()

dog1 = Dog(name="Jerry", breed="Jerman Shepherd")

dog1.breed
