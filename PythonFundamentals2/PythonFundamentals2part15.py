#  For loop (definition):
# A for loop is used to repeat a block of code a fixed number of times by iterating over 
# a sequence (like numbers, list, etc.)

# Q. Write a Python program to print each character of a string 
# and check whether a given character is present in the string.

string = "Hello"
# in => membership operator => It is used to check presences
for var in string:
    print(var)

if 'o' in string:
    print("o exists in string")

# Print numbers from 1 to 5 using for loop
for i in range(5):
    print(i+1)