"""
number guessing game.
we will have a secret number -> 3
user will have 2 trials to get the number
if they do we congratulate them, if they do not we will end the game and tell them they failed
"""
secret_number = 3
number_of_tries = 0
max_tries = 2

while number_of_tries < max_tries:
  user_guess = int(
        input("Guess the secret number from 1 - 5 (you only have 2 tries): "))

  if user_guess == secret_number:
    print(f"Congrats, you guessed the secret number: {secret_number}")
    break

  number_of_tries += 1
  if number_of_tries < max_tries:
    print("Try again.")
  else:
    print("You could not guess the secret number. You failed.")
