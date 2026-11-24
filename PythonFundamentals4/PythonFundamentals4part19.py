# Concept: Abstraction
# Create an Abstract class Employee with an abstract method
# calculate_salary().
# Create subclasses Intern, FullTimeEmployee and ContractEmployee that
# implement the method differently.

from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary():
        pass
    
class Intern(Employee):
    def calculate_salary(self):
        stipend = 10000
        print("Intern salary:", stipend)

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        salary = 50000
        print("Full-time salary:", salary)


class ContractEmployee(Employee):
    def calculate_salary(self):
        hours = 20
        rate = 500
        print("Contract salary:", hours * rate)

# Objects
i = Intern()
f = FullTimeEmployee()
c = ContractEmployee()

i.calculate_salary()
f.calculate_salary()
c.calculate_salary()

