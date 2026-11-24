# Write a function to return the count the number of digits in a number, n
def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

print(count_digits(12345))