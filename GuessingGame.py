"""
Author:     Sunil Krishnan
Date:       24-Apr-2016
Name:       GuessingGame.py
Reference:  http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
Problem Statement:
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed
too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)
Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random

if __name__ == '__main__':
    v_count = 0
    v_input = 'Guess'
    v_num = random.randint(1,10)
    while v_input != 'exit':
        v_guess = int(input('Please take a guess between 1 to 9: '))
        if v_guess < v_num:
            print('Your guess is low, guess higher')
            v_count +=1
            v_input = str('Please type exit to end else continue')
        elif v_guess > v_num:
            print('Your guess is high, guess lower')
            v_count +=1
            v_input = str('Please type exit to end else continue')
        else:
            print('You guessed right')
            v_count +=1
            break
    print('You have made '+str(v_count)+' guesses!')
