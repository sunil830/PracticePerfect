"""
Author:     Sunil Krishnan
Date:       19-Apr-2016
Name:       StringLists.py
Reference:  http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
Problem Statement:
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""

if __name__ == '__main__':
    var_inp = str(input('Please enter a string: ')).upper()
    print('The actual string is: ' + str(var_inp))
    var_reverse = var_inp[::-1]
    print('The reverse of the input string: ' + str(var_reverse))
    if var_inp == var_reverse:
        print('String is palindrome: '+str(var_inp))
    else:
        print('Nay! The string aint palindrome: '+str(var_inp))
