"""
Author:     Sunil Krishnan
Date:       17-Apr-2016
Name:       ListOverlap.py
Reference:  http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
Problem Statement:
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
Extras:
Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""
import random


def findlistoverlap(a, b):
    print([x for elem in a for x in b if elem == x])


def randomlist():
    v_num = int(input('Enter the number of elements you want in the generated list: '))
    a = random.sample(range(100), v_num)
    b = random.sample(range(100), v_num)
    findlistoverlap(a, b)


def staticlist():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    findlistoverlap(a, b)


if __name__ == '__main__':
    v_yes_no = str(input('Enter Y for Random List and N for Static List: '))
    if v_yes_no == 'Y':
        randomlist()
    else:
        staticlist()
