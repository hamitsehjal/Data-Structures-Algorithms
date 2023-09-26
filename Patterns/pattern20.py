'''
PROBLEM: Symmetric Void Pattern

Input Format: N = 3
Result: 
******
**  **
*    *
*    *
**  **
******

Input Format: N = 6
Result:   
************
*****  *****
****    ****
***      ***
**        **
*          *
*          *
**        **
***      ***
****    ****
*****  *****
************
'''


def symmetric_void_pattern(count):
    '''
    for a given value of 'N', print the symmetric void pattern
    '''

    for i in range(0, count):

        # print stars

        for _ in range(0, count-i):
            print('*', end='')

        # print spaces
        for _ in range(0, 2*i):
            print(' ', end='')

        # print stars
        for _ in range(0, count-i):
            print('*', end='')
        print()

    for i in range(0, count):
        # print stars
        for _ in range(0, i+1):
            print('*', end='')

        # print spaces
        for _ in range(0, 2*count-(2*i+2)):
            print(' ', end='')

        # print stars
        for _ in range(0, i+1):
            print('*', end='')
        print()


symmetric_void_pattern(6)
