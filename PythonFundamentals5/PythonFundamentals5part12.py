f = open("example.txt", "r")
word = "Python"
line_number = 1

for line in f:
    if word in line:
        print("The word Python Exists")
        print("line number = ", line_number )
    line_number += 1

f.close()


    
