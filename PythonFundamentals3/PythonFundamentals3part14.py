# Ask the user for a string and check whether it is a palindrome or not.
# A palindrome is a string which is same when we read it forward and 
# backward. 
# Eg - "madam" , "racecar" etc
# Hint - A palindrome string is equal to the reversed version of the string.
# We can use a loop to reverse the string manually.

# Using loop
string = input("Enter the string : ") 
reverse_string = " "
for ch in string:
    reverse_string = ch + reverse_string
print(reverse_string)

# Using slicing
str = input("Enter the string : ")
rev_str = str[ : : -1 ]
print(rev_str)
