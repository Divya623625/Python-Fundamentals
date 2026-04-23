# Given a tuple of integers, create
# A tuple of all even numbers
# A tuple of all odd numbers

tup = (1,2,3,4,5,6,7,2,4,10,21,23,86,67)
even = []
odd = []
for i in tup:
    if (i % 2 == 0):
        even.append(i)
    else: 
        odd.append(i)

even = tuple(even)
odd = tuple(odd)

print(even)
print(odd)