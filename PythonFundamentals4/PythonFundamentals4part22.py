# Concept: Multiple Inheritance
# Create the following classes: Herbivore, Carnivore, Omnivore with some
# attributes & methods. Then create a class Bear that inherits from all the above
# classes to showcase how multiple inheritance works.

class Herbivore:
    def eat_plants(self):
        print("Eats plants")

class Carnivore:
    def eat_meat(self):
        print("Eats meat")

class Omnivore:
    def eat_both(self):
        print("Eats plants and meat")

class Bear(Herbivore, Carnivore, Omnivore):
    def info(self):
        print("Bear is omnivore animal")

# Object
b = Bear()

b.eat_plants()
b.eat_meat()
b.eat_both()
b.info()