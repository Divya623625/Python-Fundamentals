#  OOP (Object-Oriented Programming) in Python is a programming style that organizes code 
#  using objects and classes. 
#  It helps make code reusable, modular, and easier to manage.

#  Procedural Oriented Programming (POP)
#  A programming style where the program is written as a set of functions (procedures) that 
#  perform tasks step-by-step.

# OOPS (Object-Oriented Programming System) = a way of writing programs using objects (real-world things)
# Instead of writing everything step-by-step (like POP), we create objects with data + functions together

# Main concepts 
# Class → blueprint (like a design)
# Object → real thing made from class
# Encapsulation → data + function in one place
# Inheritance → one class using another class features
# Polymorphism → same function, different behavior

# Example
# Class = Car design
# Object = Your actual car 

# A class is like a blueprint or template for creating objects.
# 🔹 Class and Object (very simple)
# 🔸 Class

# A class is a blueprint/template.
# 👉 It tells what properties and actions something should have.

# Example:
# class Student:
#     pass
# 🔸 Object

# An object is a real thing created from the class.
# s1 = Student()
# s2 = Student()

# 👉 s1, s2 are objects

# Easy Real-Life Example
# Class = Mobile design 
# Object = Your phone, my phone

# Difference between Function and Method 
# Function
# Independent (not inside a class)
# Called directly

# Method
# Defined inside a class
# Called using an object

class Student:
    subject = "Python"
    college = "ABC"
    year = "4th year"

a = 10
stu1 = Student()
stu2 = Student()
print(stu1)
print(stu2)
print(stu1.subject, stu1.college, stu1.year)
print(stu2.subject, stu2.college, stu2.year)

l = [1, 2]
print(type(l))

s = set()
print(type(s))

print(type(stu1))