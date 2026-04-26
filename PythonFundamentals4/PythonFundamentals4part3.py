class Student:
    college_name = "ABC College" # class attributes
    PI = 3.1
    
    def __init__(self,name,cgpa): # instance attributes
        self.name = name
        self.cgpa = cgpa
        self.PI = 3.14

stu1 = Student("Divya", 9.9)

print(stu1.name)
print(Student.college_name)
print(stu1.college_name)
print(stu1.PI)