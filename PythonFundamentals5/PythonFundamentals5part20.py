# Create a program that:
# 1. Opens a file "log.txt" in append mode
# 2. Adds a new log entry (like "Program run successfully")
# 3. Opens the file in read mode and print all logs

# Step 1: open in append mode and add log
file = open("log.txt","a")
file.write("Program run successfully\n")
file.close()

# Step 2: open in read mode and print logs
file = open("log.txt","r")
for line in file:
    print(line.strip())
file.close()
