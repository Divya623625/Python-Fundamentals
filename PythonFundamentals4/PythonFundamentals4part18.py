# Concept: Inheritance
# Create a class Vehicle with attributes like brand and model.
# Create two subClasses Car and Bike that add extra attributes - seats (in Car) &
# engine_cc (in Bike)

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats


class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc


# Objects
c = Car("Toyota", "Innova", 7)
b = Bike("Yamaha", "R15", 155)

print(c.brand, c.model, c.seats)
print(b.brand, b.model, b.engine_cc)