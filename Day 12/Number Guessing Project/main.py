from art import logo
import random


def level_checker(guess, number):
    if guess > number:
        return 'high'
    else:
        return 'low'


def play(life):
    guessed = True
    number = random.randint(1, 100)
    while guessed:
        print(f"You have {life} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))

        if guess != number:
            life -= 1
            guess_level = level_checker(guess, number)
            print(f"Too {guess_level}")
            print("Guess again")
            if life < 1:
                print(f"Too {guess_level}")
                print("You've run out of guesses, you lose")
                print(f'The number was: {number}')
                guessed = False
        if guess == number:
            print(f"You got it! The answer was {number}")
            guessed = False


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == 'easy':
    life = 10
    play(life)
elif level == 'hard':
    life = 5
    play(life)
else:
    print('Invalid difficulty')
