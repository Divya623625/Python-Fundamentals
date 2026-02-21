# Type conversion and type casting in Python
a=10
b=5
print(a/b) # Division always retuens float
print(type(a/b)) # Checking the data type

# Type conversion(implicit)
ans=5+10.0 #int + float => float(Python Converts automatically)
print(ans) 
print(type(ans)) 

# Type casting(explicit)
answer=int(5+10.0) # float -> int (converted manually using int())
print(answer)
print(type(answer))

ans1=int(5+10.0) #Casting - Casting is converting a value from one data type to another.
ans2=5+10.0 #Conversion
print(ans1 , type(ans1))
print(ans2 , type(ans2))

print(int("123")) # String to integer casting

val=int("123")
print(type(val))

val=bool(10) # Boolean casting
print(val,type(val))

# Boolean rules
# False = 0
# True = Non zero value

