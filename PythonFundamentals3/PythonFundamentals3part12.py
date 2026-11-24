s = {1,2,3,4,5,6,7,8}
s1 = {1,5,2}

# Adding an element
s.add(1)
print(s)

# Removing the value
s.remove(4)
print(s)

# Removes a random value
s.pop()
print(s)

# Returns new union
print(s.union(s1))

# Returns new intersection
print(s.intersection(s1))

# Empties the set
s.clear()
print(s)