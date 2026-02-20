"""
Variables in Python
x=5
a=25
a2 + b2
Variables are containers that holds a value. Variables in Python are used to store data so that we can use it later in our program. You can change the value anytime.
Example - name = "Divya P"
age = 30
PI = 3.14
In python, Variable doesn’t store the value directly
It stores a reference (address) to an object in memory

Example:
x = 10 → 10 is an object in memory, x points to it
So: variable = label, value = object in memory

Indentation in Python 
Indentation is very important in Python and Spacing also
Identifiers example=age, PI, name are identifiers 
even function names are called Identifiers
Python is Case sensitive
SQL/HTML is not Case sensitive
<body> Correct
<Body> Correct
Age, age, AGE are different in Python
$35=123 Wrong

Indentifier Rules
1. Can start with Eng letters 'A-Z', 'a-z'
2. Can start with Digits [ 0-9 ]
3. Can use Underscore_
Example -  _name
4. Names should be meaningful
Example -  city_name = "Delhi"
5. Cannot start with a number
6. Cannot start with spaces
7. Cannot use Python Keywords

"""
name = "Divya P"
age = 19
PI = 3.14
print(name, age, PI)
print("My Name is: ", name)
print("My age is: ", age)
print("PI value is: ", PI)

# We can perform operations also
print("My age is: ", age-5)

_name = 10
print(_name)

City_name = "Delhi"
print(City_name)

"""
Filename: PythonFundamentals1part2.py
Topic: Python Variables, Indentation, Identifier Rules.
Author: Divya P
Date: 20-02-2026
"""