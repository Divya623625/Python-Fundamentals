# Continue - skip the iteration
# 1 to 10
# You should skip the 3 multiples
i = 1
while (i<=10):
    if(i%3==0):
        i+=1
        continue
    print(i)
    i+=1
print("outside loop now.....")