'''
PROBLEM: The Number Pattern

Input Format: N = 3
Result: 
3 3 3 3 3 
3 2 2 2 3 
3 2 1 2 3 
3 2 2 2 3 
3 3 3 3 3

Input Format: N = 6
Result:   
6 6 6 6 6 6 6 6 6 6 6 
6 5 5 5 5 5 5 5 5 5 6 
6 5 4 4 4 4 4 4 4 5 6 
6 5 4 3 3 3 3 3 4 5 6 
6 5 4 3 2 2 2 3 4 5 6 
6 5 4 3 2 1 2 3 4 5 6 
6 5 4 3 2 2 2 3 4 5 6 
6 5 4 3 3 3 3 3 4 5 6 
6 5 4 4 4 4 4 4 4 5 6 
6 5 5 5 5 5 5 5 5 5 6 
6 6 6 6 6 6 6 6 6 6 6
'''


def numbers_pattern(count):
    '''
    For a given input 'N', print the numbers pattern
    '''
    counter = count
    for i in range(1, 2*count):
        # rows
        for j in range(1, 2*count):
            # columns
            if i == j and (i != 1 or i != 2*count-1 or j != 1 or j != 2*count-1):
                counter = counter-1

            print(f"{counter} ", end='')

        print()


numbers_pattern(6)
