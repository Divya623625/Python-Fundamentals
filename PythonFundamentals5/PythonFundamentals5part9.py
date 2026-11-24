f = open("sample.txt", "a+")
f.write("123")
print(f.read())
f.close()