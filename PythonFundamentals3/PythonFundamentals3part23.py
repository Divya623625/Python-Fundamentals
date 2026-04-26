# Ask the user for a string and print:
# All unique characters
# The count of unique characters

# take input
s = input("Enter a string: ")

# get unique characters using set
unique_chars = set(s)

# print unique characters
print("Unique characters:", unique_chars)

# print count
print("Count of unique characters:", len(unique_chars))