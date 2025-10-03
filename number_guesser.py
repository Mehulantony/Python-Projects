# A simple number guessing game in Python

import random

num_guesses = 0
low_value = int(input("Please enter a low value: "))
high_value = int(input("Please enter a high value: "))
computer_guess = random.randint(low_value, high_value)

print("Computer has guessed! What might be the random number?")

while num_guesses < 11:
    if num_guesses == 10:
        print("You have run out of attempts! Please start over")
        break
    user_guess = int(input("Take a guess: "))
    if user_guess > computer_guess:
        num_guesses += 1
        print("Too high! Try again")
    elif user_guess < computer_guess:
        num_guesses += 1
        print("Too low! Try again")
    else:
        print(f"You have guessed correctly.The correct number is {computer_guess}")
        break





