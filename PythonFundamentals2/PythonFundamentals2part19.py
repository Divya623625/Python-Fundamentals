# Print sum of n natural numbers

n = int(input("Enter the number: "))
sum = 0
for i in range(1,n+1):
    sum += i # count = count + i
print("The sum of",n,"natural numbers is :", sum)

# Math formula => (n * (n + 1))/2

n = int(input("Enter the number: "))
total = (n * ( n + 1 ))/2 
print("The sum of",n,"natural numbers is :", total)

