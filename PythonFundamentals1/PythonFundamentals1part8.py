#Compatable data types
"""
int - float
float - int
int - bool
"abc123" - int - wrong
"123" - int(123)

Two types
a. Type conversion - implicit type conversion
b. Type casting - explicit type conversion - developer will do this
In Python, type casting and type conversion are related but slightly different:

1. Type Casting -
   * It is the explicit conversion of one data type to another.
   * You, as the programmer decide to convert it.
   * Example:
     x = 10       # int
     y = float(x) # explicitly casting int to float
     print(y)     # 10.0

2. Type Conversion-
   * It is the implicit conversion (also called type coercion) done automatically by Python.
   * Example:
     x = 5        # int
     y = 2.5      # float
     z = x + y    # Python automatically converts x to float
     print(z)     # 7.5
    
"""
a=10
b=5
print(a/b)
print(type(a/b))

ans=5+10.0
print(ans)
print(type(ans))

#33.33 - 33 - float+int=float
#Casting - int(),float(),bool()

answer=int(5+10.0)
print(answer)
print(type(answer))

ans1=int(5+10.0) #Casting - Casting is converting a value from one data type to another.
ans2=5+10.0 #Conversion
print(ans1 , type(ans1))
print(ans2 , type(ans2))

print(int("123"))

val=int("123")
print(type(val))
val=bool(10)
print(val,type(val))
#False = 0
#True = Non zero value

"""
Filename: PythonFundamentals1part8.py
Topic: Python Type Casting and Conversion
Author: Divya P
Date: 20-02-2026
"""