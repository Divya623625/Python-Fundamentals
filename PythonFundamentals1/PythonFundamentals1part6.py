"""
Operators:
A symbol that performs an operation on one or more values (operands).
* Arithmetic - +, -, *, /, %, **
sum = a + b
Here a and b are operands
+ is an operator
= is an assignment operator
* Relational / Comparision
* Assignment
* Logical
"""

# Arithmetic Operators - used for mathematical calculations
a = 10
b = 5
print(a+b) #Addition
print(a-b) #Subtraction
print(a*b) #Muliplication
print(a/b) #Division
print(a%b) #Modulus -Remainder
print(a**b) #power(Exponent)

#Relational Operators - >,<,>=,<=,==,!= - Returns True/False - boolean - Used to Compare two values
c=10
d=5
print(c<d) #less than
print(c>d) #greater than
print(c<=d) #less than or equal to
print(c>=d) #greater than or equal to
print(c==d) #equal to
print(c!=d) #not equal to

#Assignment Operators : =, +=, -=, *=, /=, %= : a=b : Like assign -+ - used to assign values to variables
# a = 5: a+=1 : a=a+1: 5+1
a=10
a=a+5 #15
b-=5
c*=5
d/=5
e=10
e%=2
f=15
f**=2
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Logical Operators - and, or, not - Used to combine the conditions
var = False
print(not var)
print(not(5>8))

#and - two operations
# True and True = True
# True and False = False
# False and False = False
# False and True = False
print(( 5>3) and (3>2 ))
print((5>3) and (2>3))
print((5<3) and (2<3))
print((2>3) and (5<2))

#or
# True and True = True
# True and False = True
# False and False = False
# False and True = True
print(( 5>3) or (3>2 ))
print((5>3) or (2>3))
print((5<3) or (2<3))
print((2>3) or (5<2))

#Bitwise Operators
#Bitwise Operators work on binary numbers - work on bits
x = 5
y = 3
print(x & y) #0101 & 0011 = 0001 = 1 [Both bits must be 1] - Bitwise and
print(x ^ y ) # [Only 1 Bit should be 1 like both should be different] = 0101 ^ 0011 = 0110 = 6 - Bitwise xor 
print(~x) #0101 - ~a = -(a+1) - Bitwise Not
print(x | y) #0101 | 0011 = 0111 = 7 [Both bits must be 0 the result is 0] - Bitwise Or
print(x<<1) #Left shift - 0101 - 1010 - 10 
print(x>>1) #Right Shift - 0101 - 0010 - 2

#Membership Operators - Membership Operators check whether a value is present in a list, tuple, string, etc
'''in - Present
not in - Not Present in
'''
fruits = [ "apple","banana","mango"]
print("apple" in fruits)
print("grape" in fruits)
print("grape" not in fruits)

#String Example
name="Divya"
print("D" in name)
print("z" in name)

#Assignment Question
x=3
x+=5
print(x)

# Unary Operator
"""
Definition: Unary operators work on one operand.
Unary Plus (+) – keeps the value same
a = 5
print(+a)

Unary Minus (-) – changes the sign
a = 5
print(-a)

Logical NOT (not) – reverses True/False
x = True
print(not x)

Bitwise NOT (~) – flips bits
a = 5
print(~a)

🔹 Note: Python has no ++ or -- operators.

Conditional Operator
Conditional operator executes one of two expressions based on a condition.

Syntax:
result = value_if_true if condition else value_if_false

Example:
Largest of Two Numbers
a, b = 10, 20
print(a if a > b else b)
"""

"""
Filename: PythonFundamentals1part6.py
Topic: Python Operators and its types
Author: Divya P
Date: 20-02-2026
"""
