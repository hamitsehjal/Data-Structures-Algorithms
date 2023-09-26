'''
*
**
*** 
****
*****
******  
*****
****
***    
**
*
'''


def half_diamond(count):
    '''
    For a given number N, prints Half Diamond pattern
    '''
    for i in range(1, 2*count):
        if i <= count:
            print('*'*i)
        else:
            print('*'*((2*count)-i))


print("\nThis is for INPUT-5\n")
half_diamond(5)

print("\nThis is for INPUT-6\n")
half_diamond(6)

print("\nThis is for INPUT-3\n")
half_diamond(3)
