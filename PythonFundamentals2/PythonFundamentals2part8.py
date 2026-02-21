"""
Built-in and user-defined
print()       sum
input()       calc_avg
type()        ......
range()       ......
range(start, stop, step) => Optional
lambda a,b,c:  _____a+b+c => Expression
Lambda function (Python) 
A lambda function is a small, one-line function without a name.
Used when you need a function only once.
lambda arguments : expression
"""
sum=lambda a,b: a+b
print(sum(4,5))

avg=lambda a,b: (a+b)/2
print(avg(4,5))

# usage of lambda => High order fnx
# () => fnx
# return => fnx 
# def fun():
#   ________
#   ________ 

# WAF to print factorial of n:
# n=5
# 1*2*3*4*5 => 120
# 5!=120
# n!=>1*2*3*4*5*6.....*n
# fact = 1
# for i in range(1,n+1):
#    fact=fact*i
# print

def calc_factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

n=int(input("Enter n: "))
print(calc_factorial(n))