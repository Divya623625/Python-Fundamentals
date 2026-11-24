# Q10.Take a decimal number as input (like 45.78) and output its:
# integer part - 45
# fractional part - .78
num = input("Enter a decimal number: ")
integer_part, fractional_part = num.split(".")
print("Integer part:", integer_part)
print("Fractional part: ." + fractional_part)