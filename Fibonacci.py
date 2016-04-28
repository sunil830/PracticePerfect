"""
Author:     Sunil Krishnan
Date:       28-Apr-2016
Name:       Fibonacci.py
Reference:  http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
Problem Statement:
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence
is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""


def user_input():
    v_input = int(input('Please enter a number for the sequence: '))
    print('The quantum of numbers generated in the sequence is: ' + str(v_input))
    gen_fibo(v_input)


def gen_fibo(num):
    if num is not None:
        v_first = 1
        v_next = 1
        target_list = [v_first, v_next]
        count = 0
        while count <= num:
            v_sum = v_first + v_next
            target_list.append(v_sum)
            v_first,v_next = v_next,v_sum
            count += 1
        print('The fibonacci series is: ' + str(target_list))
    else:
        print('Since there is no input no series will be generated')


if __name__ == '__main__':
    user_input()
    print('Program Ends')
