#Number Guessing Game on May 08th 2025

import random



def num_guess_game():
    num_to_guess=random.randint(1,50)
    attempts=0

    print("Welcome to Number Guessing Game")
    print("Guess a number between 1 to 50")

    while True:
        try:
            guess=int(input("Enter your guess: "))
            attempts+=1

            if guess<num_to_guess:
                print("Too Low, Try Again!")
            elif guess>num_to_guess:
                print("Too High, Try Again!")
            else:
                print(f"Congratulations,you guessed the number in {attempts} attempts")
                break
        except ValueError:
            print("Please Enter a valid number")
num_guess_game()
