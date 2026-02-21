# Q4. The user enters a string containing a number (e.g., "45").Convert it to:
# An integer
# A float
# A string again
# Print all three values with their types

# Take input from user
num_1=input("Enter the number: ")
# Convert to integer
num_2=int(num_1)
# Convert to float
num_3=float(num_1)
# Convert back to string
num_4=str(num_1)
print(num_2,type(num_2))
print(num_3,type(num_3))
print(num_4,type(num_4))
