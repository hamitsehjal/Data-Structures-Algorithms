'''
PROBLEM: Alpha Ramp Pattern
Input Format: N = 3
Result: 
A
B B
C C C

Input Format: N = 6
Result:   
A 
B B
C C C
D D D D
E E E E E
F F F F F F
'''


def alpha_ramp_pattern(count):
    '''
    For a given input N, print Alpha Ramp Pattern
    '''
    counter = 'A'
    for i in range(0, count):
        for _ in range(0, i+1):
            print(f"{counter} ", end='')

        counter = chr(ord(counter)+1)
        print()


alpha_ramp_pattern(21)
