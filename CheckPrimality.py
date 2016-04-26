"""
Author:     Sunil Krishnan
Date:       26-Apr-2016
Name:       CheckPrimality.py
Reference:  http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
Problem Statement:
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to
[Exercise 4](/exercise/2014/02/26/04-divisors.html to help you.
Take this opportunity to practice using functions, described below.
"""


def user_input(help_text='Please enter a number whose primality needs to be checked: '):
    v_input = int(input(help_text))
    return v_input


def check_primality(num):
    v_elems = range(2, num)
    div_cnt = 0
    nondiv_cnt = 0
    for elem in v_elems:
        if num % elem != 0:
            nondiv_cnt += 1
        else:
            div_cnt += 1
    if div_cnt >= 1 and num != 2:
        print('The number: ' + str(num) + ' is not prime')
    else:
        print('The number: ' + str(num) + ' is prime')

if __name__ == '__main__':
    check_primality(user_input())
