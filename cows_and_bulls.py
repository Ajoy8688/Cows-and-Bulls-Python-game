import random

# Generate a secret number
number = str(random.randint(100, 999))

while len(set(number)) != 3:
    number = str(random.randint(100, 999))

# Player details
name = input("Enter your name: ")
print(f"Welcome {name} to the Bulls and Cows Game!")

chances = 10

# Game loop
while chances > 0:

    guess = input("Guess a three-digit number: ")

    # Input validation
    if len(guess) == 3 and guess.isascii() and guess.isdigit() and len(set(guess)) == 3 and guess[0] != "0":
        print("Valid guess!")
    else:
        print("Invalid guess! Try again.")
        continue

    # Reset counters
    bulls = 0
    cows = 0

    # Calculate Bulls and Cows
    for i in range(3):
        if number[i] == guess[i]:
            bulls += 1

        elif guess[i] in number:
            cows += 1

    print(f"Bulls: {bulls}")
    print(f"Cows: {cows}")

    chances -= 1

    # Winning condition
    if bulls == 3:
        print(f"Congratulations {name}! You won!")
        break

    print(f"Remaining chances: {chances}")

# Losing condition
if chances == 0 and bulls != 3:
    print("Game Over! You lost.")
    print(f"The secret number was {number}")

