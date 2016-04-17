"""
Author:     Sunil Krishnan
Date:       17-Apr-2016
Name:       ListLessThanTen.py
Reference:  http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
Problem Statement:
Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
Extras:
Instead of printing the elements one by one, make a new list that has all the elements
less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the
original list a that are smaller than that number given by the user.
"""

if __name__ == '__main__':
    v_user_option = input("Please provide an option from Display(D)/Redirect(R) : ")
    v_compare = int(input("Please input an integer to compare the list elements with : "))
    v_flow = input("Please let the program know if it has to follow the one liner(O) / Conventional Path (C): ")
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    if v_user_option == 'D':
        print('You chose to display the results')
        if v_flow == 'O':
        # The below is a one liner to print the list
            print('One Liner output is: '+str([elem for elem in a if elem < v_compare]))

        # The below commented code achieves the same functionality as the one liner
        # in a conventional for loop
        else:
            print('Printing All the elements of the list that are lesser than 5')
            for elem in a:
                if int(elem) < v_compare:
                    print(elem)
    else:
        new_list = []
        if v_flow == 'C':
            for elem in a:
                if elem < v_compare:
                    new_list.append(elem)
            print('New list : new_list[] is: '+str(new_list))
        else:
            [new_list.append(elem) for elem in a if elem < v_compare]
            print('New List: new_list[] contains: ' + str(new_list))
