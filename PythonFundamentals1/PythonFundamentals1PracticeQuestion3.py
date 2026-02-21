# Q3. Ask the user to enter two integers and one float. Convert them all to floats and print their average
# Ask the user for input
Val1=int(input("Enter value1: "))
Val2=int(input("Enter value2: "))
Val3=float(input("Enter value3: "))
# convert to float
Val1=float(Val1)
Val2=float(Val2)
# calculate average
Average=(Val1+Val2+Val3)/3
# print average
print(f"The Average is: {Average}")