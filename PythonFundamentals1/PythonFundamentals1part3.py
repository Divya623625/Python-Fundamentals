'''
Definition of Data Type
A data type defines the type of value a variable can store and what operations can be done on it.
Example - int stores whole numbers, str stores text, etc.
Integer - +ve and -ve
String - Text
Float - Decimal values - 3.14 or 4.99
Boolean - True or False - T and F Should be capital
None - No value or Nothing

📘 Python Data Types 
1. int
* Stores whole numbers
* Example: a = 10

2. float
* Stores decimal numbers
* Example: b = 3.14

3. complex
* Stores real + imaginary numbers
* Example: c = 2 + 3j

4. bool
* Stores True or False
* Example: is_ok = True

5. str
* Stores text (characters)
* Written inside quotes
* Example: name = "Divya"

6. list
* Ordered, changeable
* Written using []
* Example: marks = [80, 90, 85]

7. tuple
* Ordered, not changeable
* Written using ()
* Example: point = (10, 20)

8. set
* Unordered, no duplicate values
* Written using {}
* Example: ids = {1, 2, 3}

9. dict
* Stores data as key : value pairs
* Written using {}
* Example: student = {"name": "Divya", "age": 18}

Python decides the data type automatically
Example: x = 5 → int, x = "hi" → str

'''
name ="Divya P"
age = 19
PI = 3.14
num = 2
isPrime = True
is_Prime = None

print(type(isPrime))
print(type(is_Prime))
print(type(age))
print(type(name))
print(type(PI))

"""
Filename: PythonFundamentals1part3.py
Topic: Python Datatypes
Author: Divya P
Date: 20-02-2026
"""