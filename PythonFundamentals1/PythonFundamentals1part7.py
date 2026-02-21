#Operator precedence means priority - It tells which operator is executed first in an expression.
#(BODMAS)
#High to Low
# Associativity means it tells direction of execution when operators have same precedence
"""
() -> Left - Right
** -> Right - Left
+x,-x,~x -> Left - Right
*,/,%,// -> Left - Right
+,- -> Left - Right
<<,>> -> Left - Right
& -> Left - Right
| -> Left - Right
is,is not,in,not in,==,!=,>,<,>=,<= -> Left - Right
not -> Left - Right
and -> Left - Right
or -> Left - Right
if else -> Left - Right
lambda -> Left - Right
=,+=,-=,*=,/= -> Right - Left

3 * 5 + 2
 |   |
15 + 2 = 17 
 or
3  * 7 = 21

Same precedence [Left to Right]
10/2*5
5*5=25

Filename: PythonFundamentals1part7.py
Topic: Python Precedence and Associativity
Author: Divya P
Date: 20-02-2026


"""