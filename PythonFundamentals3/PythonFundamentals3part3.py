# Formatting
# String formatting = putting values inside a string

a = 5
b = 10
sum = a + b

# Normal formatting
print("sum of {} and {} is {}".format(a,b,sum))
print("language is {}".format("Python"))

# Index based formatting
print("sum of {1} and {0} is {2}".format(a,b,sum))

# Value based formatting
print("values of vars {a} and {b}".format(a=5,b=10))

# f-string = easy way to put variables inside a string
c = 5
d = 10
print(f"sum of {c} and {d} is {c+d}")
print(f"average of {c} and {d} is {(c+d)/2}")
