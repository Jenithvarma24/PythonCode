# random number 1 to 10 ask user to guess it
import random

secret_number = random.randint(1, 10)

while True:
    guess = int(input("Guess the number between 1 and 10: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")
        break