'''
PROBLEM: Reverse Letter Triangle Pattern
Input Format: N = 3
Result: 
A B C
A B
A

Input Format: N = 6
Result:   
A B C D E F
A B C D E 
A B C D
A B C
A B
A
'''


def reverse_letter_triangle(count):
    '''
    For a given input 'N', prints the reverse letter triangle pattern
    '''
    for i in range(0, count):
        counter = 'A'
        for _ in range(0, count-i):
            print(f"{counter} ", end='')
            counter = chr(ord(counter)+1)

        print()


reverse_letter_triangle(28)
