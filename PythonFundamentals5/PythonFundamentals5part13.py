data = True
line = 1
word = "Python"

with open("example.txt","r") as f:
    while data:
        data = f.readline()

        if(word in data):
            print(f"{word} found at line {line}")
            break

        print(data)
        line += 1