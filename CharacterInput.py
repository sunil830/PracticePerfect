"""
Author:     Sunil Krishnan
Date:       16-Apr-2016
Name:       CharacterInput.py
Reference:  http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
Problem Statement:
To Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells
them the year that they will turn 100 years old.
Extras:
Add on to the previous program by asking the user for another number
and printing out that many copies of the previous message.
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)
"""
import datetime


def userturnshundred(v_age):
    """
    :param v_age:
    Using datetime to get the current year
    """
    v_fut_year = datetime.datetime.now().year + (100 - int(v_age))
    return v_fut_year


def userinput():
    v_name = input('Please enter your name:')
    print('Your Name as you entered it is:' + v_name)
    v_age = input('Please enter your age as a number:')
    print('Your Age as you entered it is:' + v_age)
    v_mesg = input('Please enter a number greater than 1: ')
    v_years = userturnshundred(v_age)
    print(int(v_mesg) * (v_name+' ,You would be 100 years old in ' + str(v_years) + '\n'))


userinput()
