"""
Author:     Sunil Krishnan
Date:       19-Apr-2016
Name:       ListComprehension.py
Reference:  http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
Problem Statement:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has
only the even elements of this list in it.
"""

if __name__ == '__main__':
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = [x for x in a if x % 2 == 0]
    print(b)
