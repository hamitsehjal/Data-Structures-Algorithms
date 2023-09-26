'''
PROBLEM: Symmetry Butterfly Pattern

Input Format: N = 3
Result: 
*    *
**  **
******
**  **
*    *


Input Format: N = 6
Result:   
*          *
**        **
***      ***
****    ****
*****  *****
************
*****  *****
****    ****
***      ***
**        **
*          *

How many rows we'll have?? - if n is 6, we have 11 rows. if n is 3, we have 5: Formula is : 2*N-1
if n=6, we'll have 12 columns in each row. In the first row, we will always 1 star on each and rest are spaces

Spaces start from 2*N-2; IF n is 6, spaces will start with 10
spaces decrement by 2

Stars matches the row. if we are on row 1, we have one star

once we surpass the row i.e more than N
SPACES increment by 2
stars decrement by 1

'''


def symmetry_butterfly_pattern(count):
    '''
    for a given number of N, print the symmetry butterfly pattern
    '''
    stars = 1
    spaces = 2*count-2

    for i in range(0, 2*count-1):
        # print(f"i: {i} - Stars: {stars} - Spaces: {spaces}")
        # print the stars
        for _ in range(0, stars):
            print('*', end='')

        # print the spaces
        for _ in range(0, spaces):
            print(' ', end='')

        # print the stars
        for _ in range(0, stars):
            print('*', end='')

        spaces = spaces+2 if i >= (count-1) else spaces-2
        stars = stars-1 if i >= (count-1) else stars+1

        print()


symmetry_butterfly_pattern(7)
