# Let's create a simple calculator that performs arithmetic operations. Create a function 
# calculator(a,b,operation) that performs addition, subtraction, multiplication, or division 
# based on the operation parameter
# [ operation parameter can have values '+', '-', '*','/']

def calculator(a,b,operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b!=0:
            return a/b
        else:
            return "Error: division by zero"
    else:
        return "Invalid Operation"

# Example usage
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation(+,-,*,/): ")
result = calculator(num1,num2,op)
print("Result", result)
    