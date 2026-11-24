# Input two list of integers from the user. 
# Merge them into one list and sort the result.
# Eg - list1 = [ 1,2,7 ], list2 = [ 2,4,5 ]
# result = [ 1,2,2,4,5,7 ]

# List 1
list1 = []
m = int(input("Enter the number of elements : "))
for i in range(m):
    num1 = int(input("Enter number : "))
    list1.append(num1)
print(list1)

# List 2
list2 = []
n = int(input("Enter the number of elements : "))
for j in range(n):
    num2 = int(input("Enter number : "))
    list2.append(num2)
print(list2)

result = list1 + list2
result.sort()
print(result)


