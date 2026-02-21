#Odd numbers without continue
i = 1
while (i<=10):
    print(i)
    i+=2

#Odd num using continue
i = 1
while (i<=10):
    if (i%2==0):
        i+=1
        continue
    print(i)
    i+=1

# Odd nums
i=0
while(i<10):
    i+=1
    if(i%2==0):
        continue
    print(i)