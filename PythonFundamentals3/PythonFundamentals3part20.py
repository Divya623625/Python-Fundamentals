# Write a program that takes a string from the user and prints the number of spaces in the string.
string = input("Enter the string : ")
spaces = 0
for ch in string:
    if(ch == " "):
        spaces += 1
        
print(spaces)