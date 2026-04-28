# File I/O (Input/Output) in Python is used to read data from files and write data to files. 
# It’s a core concept for handling data persistence.

# File operations
# r = readind [default]
# w = writing, truncates file first = overwrites
# x = creates new and open for writing = throws the error if file already exists
# a = writing, appends at end
# b = binary mode
# t = text mode [default]
# + = opens disk file for update(r and w) 

# Open the file to read
f = open("sample.txt", "r") # f = returns file object 
print(f)

# Take everything from file and store it and it reads entire file
data = f.read()

# Displays the file content on screen
print(data)
print(type(data))

f.close()

