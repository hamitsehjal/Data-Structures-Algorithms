'''
Pattern – 12: number Crown Pattern

1    1
12  21
123321
'''


def number_crown_patter(count):
    '''
    For a given input 'n', print the number crown pattern
    '''
    for i in range(0, count):

        # print numbers
        for j in range(0, i+1):
            print(j+1, end="")

        # print spaces
        for _ in range(0, 2*count-(2*(i+1))):
            print(' ', end="")
        # print numbers
        for j in range(i+1, 0, -1):
            print(j, end="")

        print()


# number_crown_patter(6)
number_crown_patter(10)
