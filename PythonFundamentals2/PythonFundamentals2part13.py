#Write a python program that prints numbers from 1 to 10 but uses a
#break statement to stop the loop early if the number is divisible by 6.
i=1
while i <= 10:        # while loop starts
    if i % 6 == 0:    # inside while
        break         # inside if (and while)
    print(i)          # inside while (NOT inside if)
    i += 1            # inside while - updation

print("Outside loop now......") # outside while
