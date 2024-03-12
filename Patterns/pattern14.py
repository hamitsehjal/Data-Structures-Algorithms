'''
PROBLEM: Increasing Number Triangle Pattern

Input Format: N = 3
Result: 
1
2 3
4 5 6

Input Format: N = 6
Result:   
1
2  3
4  5  6
7  8  9  10
11  12  13  14  15
16  17  18  19  20  21
'''


def increasing_number_triangle(count):
    '''
    For a given input N, print the increasing number triangle
    '''
    counter = 1
    for i in range(0, count):
        for _ in range(0, i+1):
            print(f"{counter} ", end="")
            counter = counter+1
        print()


increasing_number_triangle(3)
