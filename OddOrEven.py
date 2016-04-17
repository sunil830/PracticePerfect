"""
Author:     Sunil Krishnan
Date:       17-Apr-2016
Name:       OddOrEven.py
Reference:  http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
Problem Statement:
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?
Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and
one number to divide by (check). If check divides evenly into num,
tell that to the user. If not, print a different appropriate message.
"""


def acceptuserinput():
    num = input('Please enter an integer and I will tell you if it is odd or even: ')
    check = input('Please enter an integer by which I can check your number: ')
    if num is not None and int(num) != 0:
        if check is None or len(str(check)) == 0 or int(check) <= 1:
            if int(num) % 2 == 0:
                if int(num) % 4 != 0:
                    print('The number :' + str(num) + ' is an even number but not a multiple of 4')
                else:
                    print('The number :' + str(num) + ' is an even number and is a multiple of 4')
            else:
                print('The number :' + str(num) + ' is an odd number')
        else:
            if int(num) % int(check) == 0:
                print('The number you entered: ' + num + 'gets divided evenly by :' + check)
            else:
                print('The number you entered: ' + num + ' is not divided evenly by :' + check)
    else:
        print('Please provide the first non zero argument for the program to function')

acceptuserinput()
