class student:
    def __init__(self):
        print("Obj is being constructed.....")

    def __init__(self,name, cgpa): # parameterised
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa

stu1 = student("Rahul", 9.0)
stu2 = student("Divya", 8.8)
stu3 = student("Sushmitha", 10)

print(stu1.name)
print(stu2.name)
print(stu3.name)

print(stu1.cgpa)
print(stu2.cgpa)
print(stu3.cgpa)

print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")
