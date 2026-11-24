# Q6. Write a program to swap values of two numbers entered by the user
a=int(input("Enter 1st value: "))
b=int(input("Enter 2nd value: "))
a, b = b, a   # swapping
print("After swapping:")
print("a =", a)
print("b =", b)