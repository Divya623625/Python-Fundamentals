# Create a program that:
# 1. Has a list of numbers: [5, 10, 15, 20, 25]
# 2. Uses a list comprehension to create a new list with only numbers greater than 15
# 3. Prints the new list

# Step 1: original list
numbers = [5, 10, 15, 20, 25]

# Step 2: list comprehension (numbers > 15)
new_list = [num for num in numbers if num > 15]

# Step 3: print result
print(new_list)