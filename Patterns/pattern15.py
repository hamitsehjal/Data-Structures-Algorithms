'''
PROBLEM: Increasing Letter Triangle Pattern
Input Format: N = 3
Result: 
A
A B
A B C

Input Format: N = 6
Result:   
A
A B
A B C
A B C D
A B C D E
A B C D E F
'''


def increasing_letter_triangle(count):
    '''
    For a given input 'N', prints the increasing letter triangle pattern
    '''
    for i in range(0, count):
        counter = 'A'
        for _ in range(0, i+1):
            print(f"{counter} ", end="")
            counter = chr(ord(counter)+1)
        print()


increasing_letter_triangle(6)
