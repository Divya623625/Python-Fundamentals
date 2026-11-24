# Concept: Function Overriding
# Create a class Shape with a method area().
# Create subclasses Circles, Rectangle , and Triangle that override the area()
# method.

class Shape:
    def area(self):
        print("Area not defined")

class Circle(Shape):
    def area(self):
        r = 5
        print("Circle area:", 3.14 * r * r)

class Rectangle(Shape):
    def area(self):
        l = 4
        b = 3
        print("Rectangle area:", l * b)

class Triangle(Shape):
    def area(self):
        b = 4
        h = 2
        print("Triangle area:", 0.5 * b * h)

# Objects
c = Circle()
r = Rectangle()
t = Triangle()

c.area()
r.area()
t.area()