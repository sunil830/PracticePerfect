"""
Author:     Sunil Krishnan
Date:       28-Apr-2016
Name:       ListEnds.py
Reference:  http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
Problem Statement:
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""


def default_list():
    a = [5, 10, 15, 20, 25]
    b = [a[0], a[-1]]
    print('The first and last elements respectively: ' + str(b[0]) + ':' + str(b[1]))


def custom_list(v_list=None):
    if v_list is not None:
        print('The first and last elements respectively: ' + str(v_list[0]) + ':' + str(v_list[-1]))


if __name__ == '__main__':
    v_input = input('Type C for custom list or D for Default List: ').upper()
    if v_input == 'D':
        default_list()
    elif v_input == 'C':
        v_list = input('Please input your list: ')
        custom_list(v_list)
    print('Program Ends')
