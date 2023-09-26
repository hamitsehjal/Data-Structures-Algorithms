'''
Binary Number Triangle Pattern
1
01
101
0101
10101
010101

Breaking down the problem:

 - For outer loop, we know we have to iterate n times where n is the given input
 - For nested loop, for even index, we start with 1 and for odd index, we start with 0
 - For nested loop, we switch between 0 and 1 every time

1   --> 0th index, its even so we start with 1
01  --> 1th index, its odd so we start with 0
101 ,.....
0101
10101
010101

PseudoCode:
Outer loop - iterate n times where n is the given input
Nested loop 
    - iterates i+1 times where 'i' is the index of the line. If line is 1, its index is 0 so we iterate 0+1 i.e 1 time
    - If line's index is even, we start with '1' else we start with '0'
    - Inside nested loop, we switch between '1' and '0' for every iteration

'''


def binary_number_triangle(count):
    'for a given input, print the binary number Triangle Pattern'
    for i in range(0, count):
        start = 0
        if i % 2 == 0:
            start = 1
        else:
            start = 0
        for _ in range(0, i+1):
            print(f"{start}", end="")
            start = start-1 if start == 1 else start+1

        print()


binary_number_triangle(10)
