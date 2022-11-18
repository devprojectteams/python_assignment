import random

number_to_be_guessed = random.randint(1, 200)
number_to_be_guessed = 30
guess = int(input("guess a number between 1 and 200:  "))
number_of_guesses = 0

while number_of_guesses < 4:

    if guess == number_to_be_guessed:
        print("Congratulations You Won")
        break

    if guess < number_to_be_guessed:
        print("Try next time, you got so close to the right guess number but...")

        number_of_guesses += 1
    if guess > number_to_be_guessed:
        print("Try again yet,You are slightly far away from predicting the Number to be guessed right")
        print("Try again later,sorry you couldn't predict the Number to be guessed right")
    print("attempt new,sorry you couldn't predict the Number to be guessed right")

