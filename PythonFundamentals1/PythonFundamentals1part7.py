#Operator precedence means priority - It tells which operator is executed first in an expression.
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
"""
result = 10 + 20 * 3 - 4 / 2
print(result)

"""
In the given expression 10 + 20 * 3 - 4 / 2, Python first follows operator precedence, so multiplication 
and division are performed before addition and subtraction. Therefore, 20 * 3 becomes 60 and 4 / 2 becomes 
2.0. After that, Python applies associativity, solving the remaining operations from left to right. So 10 + 60 
becomes 70, and 70 - 2.0 gives the final result 68.0.
"""