# Lambda Function
# A lambda function in Python is a small, anonymous (unnamed) function defined using the lambda 
# keyword. It’s typically used for short, simple operations where defining a full function with
# def would be unnecessary.

# Basic syntax
# lambda arguments: expression
# It can take any number of arguments
# But it can only have one expression (no multiple statements)

# We use lambda functions in places where a small, temporary function is needed.

sum = lambda a,b,c: a+b+c
print(sum(4,5,10))

avg = lambda a,b: (a+b)/2
print(avg(10,10))