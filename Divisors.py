"""
Author:     Sunil Krishnan
Date:       17-Apr-2016
Name:       Divisors.py
Reference:  http://www.practicepython.org/exercise/2014/02/26/04-divisors.html
Problem Statement:
Create a program that asks the user for a number and then prints out a list of
all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly
into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""


def createdivisorlist(number):
    div_list = ([elem for elem in range(2, number) if number % elem == 0])
    return div_list


if __name__ == '__main__':
    v_num = int(input('Please enter a number for which you would like to get the divisors: '))
    print('The divisor list for the input number: '+str(v_num)+' is '+str(createdivisorlist(v_num)))
