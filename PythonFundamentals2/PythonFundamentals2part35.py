# Let’s create a "Number Guessing Game". Given a secret number (already decided by you), 
# write a program that asks the user to guess it and prints:
# "Too high" if the guess is above the number
# "Too low" if the guess is below
# "Correct!" if the guess matches

secret_number = 10 # We can change the secret number
while True:
    guess = int(input("Enter the number: "))
    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else: 
        print("Correct!")
        break