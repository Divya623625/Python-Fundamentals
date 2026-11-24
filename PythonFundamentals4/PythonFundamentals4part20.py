# Concept: Constructor Overloading (with Default Parameters)
# Create a class Person that allows the constructor to work with:
# • name only
# • name + age
# • name + age + address
# As direct constructor overloading (multiple constructors) are not allowed but
# we have to use default parameters to simulate constructor overloading.

class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)


# Different ways (like overloading)
p1 = Person("Divya")
p2 = Person("Divya", 20)
p3 = Person("Divya", 20, "Bangalore")

p1.display()
p2.display()
p3.display()
