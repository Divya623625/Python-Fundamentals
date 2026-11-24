# Added loop to print numbers and break when multiple of 6 is found
i = 1
while (i <= 10):
    if(i % 6 == 0):
        break
    print(i)
    i += 1
print("Outside loop now...")