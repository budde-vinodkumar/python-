# Number Guessing Game

secret_number = 7
attempts = 0

while True:
    guess = int(input("Guess the number (1 to 10): "))
    attempts += 1

    if guess == secret_number:
        print("Correct! You guessed it in", attempts, "attempts")
        break
    elif guess > secret_number:
        print("Too high, try again")
    else:
        print("Too low, try again")
