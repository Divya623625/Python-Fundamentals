# Write a python program to print each character of a string using a for loop and check whether 
# a specific character exists in the string using the membership operator

# For Loop - Sequential traversal 
# tuple, list, dictionary, strings: Sequence of characters
string="hello"
#in => membership operator => To check presence
for var in string:
    print(var)

if 'o' in string:
    print("o exists in string")