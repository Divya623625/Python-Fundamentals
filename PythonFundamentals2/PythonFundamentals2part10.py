""" 
Q1.Write a program that takes salary as input. Using conditional statements, 
calculate the final tax rate based on these rules:
• If salary < 30,000 → 5%
• If salary is 30,000 – 70,000 → 15%
• If salary > 70,000 → 25%
"""
salary = int(input("Enter the salary: "))
if salary < 30000:
    tax_rate=5
elif salary < 70000:
    tax_rate=15
else:
    tax_rate=25
tax=salary*tax_rate/100
print("Tax rate:", tax_rate, "%")
print("Tax amount:", tax)

""" Q2.Write a function that takes two integers a and b and prints all even numbers between them (inclusive)."""
def even_numbers(a, b):
    for i in range(a, b+1):
        if i % 2 == 0:
            print(i)

even_numbers(4, 15)

""" Q3. Write a function that prints the digits of a number n.
For eg: n=312 , there are 3 digits in it 3, 1 and 2 & we need to print them. 
Hint- The right most digit of a number N is N % 10. 
And to remove the right most digit from a number, we can do N = N / 10. """
def print_digits(n):
    while n > 0:
        digit = n % 10
        print(digit)
        n = n // 10
# Example
print_digits(312)

""" 
312 // 10 = 31
Why?
// is floor division in Python.
It divides and removes the decimal part.
So:
Normal division: 312 / 10 = 31.2
Floor division: 312 // 10 = 31 
"""

# Q4. Write a function to return the count the number of digits in a number n.
def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

print(count_digits(4567))  # Output: 4

# Q5. Write a function to return the sum of digits of a number.
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10 # n % 10 gives the last digit of n. That digit is added to total.
        n //= 10 # Divides n by 10 and removes the last digit.
    return total

# Q6.  Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5
i=0
for i in range(1,101):
    if(i % 3 == 0 and i % 5 == 0 ):
        print(i)

# Q7. Write a program to continuously input a number n from the user and print if it is positive or negative until the user enters quit
while True:
    n = input("Enter a number (or type quit to stop): ")

    if n == "quit":
        print("Program stopped")
        break

    n = int(n)

    if n > 0:
        print("Positive number")
    elif n < 0:
        print("Negative number")
    else:
        print("Zero")

# Q8. Letʼs create a Simple Calculator calculator(a, b, operation) that performs arithmetic operations. Create a function  that performs addition, subtraction, multiplication, or division based on the operation parameter. 
# [operation parameter  ‘+’ ‘-’ '*’ ‘/’ ]
def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

# Example usage
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

result = calculator(num1, num2, op)
print("Result:", result)

#Q9. Write a function is_prime(n) that returns True if n is a prime number and False otherwise, using a loop.

#Hint:
#Check prime for 2 or numbers greater than 2 (2 is the smallest prime number).
#A non-prime number n will always get divided by at least one number in the range [2, n-1].
#Example:
#For number 9, check in range (2, 8). It gets divided by 3, so 9 is non-prime → return False.
#For number 7, check in range (2, 6). It doesn’t get divided by any → return True.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
# Test
print(is_prime(7))  # True
print(is_prime(9))  # False

# 10. Create a Number Guessing Game. Given a secret number (already decided by you), write a program that asks the user to guess it and prints:

# "Too high" if the guess is above the number
# "Too low" if the guess is below
# "Correct!" if the guess matches

secret_number = 7  # You can change the secret number

while True:
    guess = int(input("Guess the number: "))
    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("Correct!")
        break
