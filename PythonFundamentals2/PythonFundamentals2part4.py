"""
print the following:
<13 - Child
13 - 18 - teenager
18+ - Adult
"""
age=int(input("Enter the age: "))
if (age<13): # wrapping up will help in readability
    print("Child")
elif (age >= 13 and age < 18): #13-18
    print("Teenager")
else:
    print("Adult")