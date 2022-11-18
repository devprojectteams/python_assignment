# number_to_be_guessed = 78

import random

number_to_be_guessed = random.randint(1, 100)
number_to_be_guessed = 78
guess = int(input("Guess a number between 1 and 100: "))
number_of_guesses = 0

number_of_guess = 1
while number_of_guesses < 3:
    if guess == number_to_be_guessed:
        print("You got it right")
        break
else:
    guess = int(input("Guess a number between 1 and 100: "))
    number_of_guesses += 1
if number_of_guesses == 3:
    print("Try again later, Its unfortunate you could not guess", number_to_be_guessed)







# import random
#
# number_to_be_guessed = random.randint(1, 100)
# number_to_be_guessed = 78
# guess = int(input("Guess a number between 1 and 100: "))
# number_of_guesses = 0
#
# number_of_guess = 1
# while number_of_guesses < 3:
#     if guess == number_to_be_guessed:
#         print("You got it right")
#         break
# else:
#     guess = int(input("Guess a number between 1 and 100: "))
#     number_of_guesses += 1
# if number_of_guesses == 3:
#     print("Try again later, Its unfortunate you could not guess", number_to_be_guessed)
