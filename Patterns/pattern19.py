'''
PATTERN: Alpha Triangle Pattern

Input Format: N = 3
Result: 
C
B C
A B C

Input Format: N = 6
Result:   
F
E F
D E F
C D E F
B C D E F
A B C D E F

BREAKDOWN:
    1. Outer loop iterates 'N' times.
    2. Initialize a counter(start) to a 'letter' based on value of 'N'
        - if N is 3, then  start is set to 'C'
    3. nested loop
        - before each nested loop, decrease the start by this formula: start=start-(i+1) where 'i' is the current level of iteration for outer loop
        - move the nested loop for the number of iterations equals to line number
        - inside nested loop, increment the start
'''


def alpha_triangle_pattern(count):
    '''
    for a given value of 'N', print the alpha triangle pattern
    '''

    for i in range(0, count):

        for j in range((ord('A')+(count-1-i)), (ord('A')+(count))):
            print(chr(j), end='')
        print()


alpha_triangle_pattern(6)
