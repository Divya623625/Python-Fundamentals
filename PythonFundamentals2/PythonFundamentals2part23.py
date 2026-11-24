# Default parameter: already has a value
# Non-default parameter: no value, must be given
def sum(a,b=5):
    return a + b

# We are passing both values, so default value is ignored.
print(sum(10,10))

# Default value (b=5) is used only when you don’t pass b.
def add(a,b=5):
    return a + b

print(add(10))
