# Arithmetic Operators - used for mathematical calculations
a = 10
b = 5
print(a+b) 
print(a-b) 
print(a*b) 
print(a/b) 
print(a%b) 
print(a**b) 

#Relational Operators - Used to Compare two values
c=10
d=5
print(c<d) 
print(c>d) 
print(c<=d) 
print(c>=d) 
print(c==d) 
print(c!=d) 

#Assignment Operators : =, +=, -=, *=, /=, %= - used to assign values to variables
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

#Bitwise Operators work on binary numbers - work on bits
x = 5
y = 3
print(x & y) 
print(x ^ y ) 
print(~x) 
print(x | y) 
print(x<<1) 
print(x>>1) 

#Membership Operators - Membership Operators check whether a value is present in a list, tuple, string, etc
'''
in - Present
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
a = 5
print(+a)

a = 5
print(-a)

x = True
print(not x)

a = 5
print(~a)

# Conditional [Ternary] Operator
a, b = 10, 20
print(a if a > b else b)
