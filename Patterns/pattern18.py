'''
PROBLEM: Alpha-Hill Pattern
Input Format: N = 3
Result: 
  A  
 ABA 
ABCBA


Input Format: N = 6
Result:   
     A     
    ABA    
   ABCBA   
  ABCDCBA  
 ABCDEDCBA 
ABCDEFEDCBA

BREAKDOWN:
    1. Outer loop iterates 'N' times
    2. For nested loop:
        - we start the counter from 'A'
        - we increment the counter until the current iterates becomes equals to current line number
        - After this point, we start decrementing the counter
'''


def alpha_hill_pattern(count):
    '''
    for a given input n, print the alpha hill pattern
    '''
    for i in range(0, count):
        # print spaces
        for _ in range(1, count-i):
            print(' ', end='')

        # print letters
        counter = 'A'
        for j in range(0, (2*i)+1):
            print(f"{counter}", end='')
            if j >= i:
                counter = chr(ord(counter)-1)
            else:
                counter = chr(ord(counter)+1)

        # print spaces
        for _ in range(1, count-i):
            print(' ', end='')

        print()


alpha_hill_pattern(6)
