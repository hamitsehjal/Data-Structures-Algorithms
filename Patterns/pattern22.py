'''
PROBLEM: Hollow Rectangle Pattern

Input Format: N = 3
Result: 
***
* *
***

Input Format: N = 6
Result:   
******
*    *
*    *
*    *
*    *
******

BREAKDOWN:
            - we are printing stars only on the borders, rest are spaces
            - We iterate N times for outer loop(N rows), N times for inner loop(N columns)
            - Figure out when do we encounter border

'''


def hollow_rectangle_pattern(count):
    '''
    For a given value of N, print the hollow rectangle pattern
    '''

    for i in range(0, count):
        for j in range(0, count):
            if i == 0 or i == count-1 or j == 0 or j == count-1:
                print('*', end='')
            else:
                print(' ', end='')

        print()


hollow_rectangle_pattern(9)
