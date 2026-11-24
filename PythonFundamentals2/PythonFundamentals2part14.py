print("Printing odd nums using continue")
i = 0
while i < 10:
    i+=1
    if (i % 2 == 0):
        continue
    print(i)
print("========================================")
print("Printing odd nums without using continue")
i = 1
while i <= 10:
    print(i)
    i+=2 