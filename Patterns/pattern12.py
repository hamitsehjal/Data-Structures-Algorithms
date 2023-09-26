'''
Pattern – 12: star Crown Pattern

*          *
**        **
***      ***
****    ****
*****  *****
************
'''


def star_crown_patter(count):
    '''
    For a given input 'n', print the star crown pattern
    '''
    for i in range(0, count):

        # print stars
        for _ in range(0, i+1):
            print('*', end="")

        # print spaces
        for _ in range(0, 2*count-(2*(i+1))):
            print(' ', end="")
        # print stars
        for _ in range(0, i+1):
            print('*', end="")

        print()


star_crown_patter(6)
