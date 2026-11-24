# Write a function that takes two integers a and b and 
# prints all even numbers between them (inclusive)
def even_numbers(a,b):
    for i in range(a,b+1):
        if(i % 2 == 0):
            print(i)

even_numbers(2,16)