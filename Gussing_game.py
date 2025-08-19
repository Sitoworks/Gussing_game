import random

print("welcome to SItoworks random Guessing game!")
secretNumber = random.randint(1, 100)
attempts = 0

while True:
    Guess = int(input("Guess a number: "))
    attempts += 1
    if Guess == secretNumber:
        print(f"Congratulations! You have guessed the correct number in {attempts} attempts")
        break
    elif Guess < secretNumber:
        print("Sitoworks: Try a higher number!")
    else:
        print("Sitoworks: Try a Lower number")