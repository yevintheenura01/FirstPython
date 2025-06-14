#set an random number between 1 and 100
import random

number = random.randint(1, 100)
#ask the user to guess the number
while True:
    guess = input('Guess a number between 1 and 100: ')
    if guess.isdigit():
        guess = int(guess)
        if guess < 1 or guess > 100:
            print('Please enter a number between 1 and 100.')
        elif guess < number:
            print('Too low! Try again.')
        elif guess > number:
            print('Too high! Try again.')
        else:
            print('Congratulations! You guessed the number!')
            break
