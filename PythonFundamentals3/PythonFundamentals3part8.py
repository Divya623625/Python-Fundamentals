# Tuple in Python:
# A tuple is a collection of items ordered + immutable (cannot change).
tuple = (1,2,3,4,5,"abc",3.15)
# tuple[3] = 30 -> Tuples cannot be changed once assigned(They are immutable)
print(tuple)
print(type(tuple))

tup = (1) # This is treated as integer, not tuple.
print(type(tup))

tup1 = ("abc") # This is treated as string, not tuple
print(type(tup1))

tuple1 = (1,) # single element tuple
print(tuple1)
print(type(tuple1))

# slicing In Tuples
tuple2 = (1,2,3,4,5,6,7,10)
print(tuple2[0:5])
print(tuple2[:len(tuple2)])

tuple3 = (1,2,3,4,5,6,7,8,9,10)

sum = 0
for val in tuple3:
    print(val)
    sum += val

print(f"Sum of values is: {sum}")

# Methods in Tuples
# t.index(val) - returns 1st occurence idx
# t.count(val) - counts total occurances
t = (1,2,3,4,5,6,7,7,5)
print(t.index(5))
print(t.count(7))
