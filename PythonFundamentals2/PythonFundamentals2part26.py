# Write a program that takes salary as input. Using conditional statements, 
# calculate the final tax rate based on these rules
# if salary < 30000 -> 5%
# If salary is 30000 - 70000 -> 15%
# If salary > 70000 -> 25%

salary = int(input("Enter the salary: "))
if(salary < 30000):
    tax_rate = 5
elif salary < 70000:
    tax_rate = 15
else:
    tax_rate = 25
tax = (salary*tax_rate)/100
print("Tax rate = ",tax_rate,"%")
print("Tax amount = ",tax)