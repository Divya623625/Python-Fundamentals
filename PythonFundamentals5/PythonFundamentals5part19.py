# Create a program that:
# 1. Opens a file "names.txt" in write mode
# 2. Writes 5 names(one per line) entered by the user
# 3. Then opens the same file in read mode and prints all names

# Step 1: write names
f = open("names.txt", "w")

for i in range(5):
    name = input("Enter name: ")
    f.write(name + "\n")

f.close()

# Step 2: read and print names
f = open("names.txt", "r")

for line in f:
    print(line.strip())  # remove extra newline

f.close()
