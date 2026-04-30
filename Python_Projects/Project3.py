# Simple Password Generator
import random
print("🔐 Password Generator")
length = int(input("Enter password length: "))
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
password = ""

for i in range(length):
    password += random.choice(chars)
print("Your Password is:", password)