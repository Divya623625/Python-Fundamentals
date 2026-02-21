# Function => Block of statements that performs a specific task => Reusable Components of code like remote
# Definition => logic
# Function Call => invoke
# def => Keyword
# def function_name():
#   __
#   __

def hello(): #Fnx definition
    print("Hello")
    print("From Python")
hello() #Fnx call
hello()

"""
parameters
logic
return

Example - sum
a,b
a+b => sum
return
def sum(a,b):
    sum=a+b
    return sum
"""
# Function definition
def sum(a, b): #parameters
    s=a+b
    return s

# Function call
ans=sum(3, 4) #arguments
print(ans)
print(sum(3,10))
print(sum(5,5))

# a,b,c - return avg
# a+b+c/3
# Calculate average
def cal_avg(a,b,c):
    sum=a+b+c
    return sum/3

print(cal_avg(5,10,15))

# Default value
"""
def sum(a,b=1):
    return a+b
sum(5) => 5+1
Non-default parameters and Default parameters
"""

def sum(a, b=1):
    return a+b
print(sum(5))