# Single Inheritance

# Parent -> Child
class Parent:
    def display(self):
        print("Parent class")
        
class Child(Parent):
        pass

c = Child()
c.display() 