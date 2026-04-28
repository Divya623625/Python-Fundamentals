# Write a program that tries to open "data.txt" in read mode. If the file does not
# exist, catch the exception and print "File not found!".

try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    print("File not found!")