# In Python, a list is a built-in data type used to store multiple items in a single variable. 
# Lists are ordered, mutable (changeable), and allow duplicate values.
# Allows mixed data types
marks = [92,98,100,67,86,95,"abc",100.86]
marks[4] = 100
print(marks)
print(len(marks))
print(marks[3])
print(marks[4])
print(type(marks))

# slicing 
print(marks[:5])
print(marks[2:5])
print(marks[5:len(marks)])
print(marks[-5:-2])