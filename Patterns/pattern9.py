'''
    *    
   ***   
  *****  
 ******* 
*********
*********
 *******
  *****
   ***
    *
'''
N = 5
for i in range(0, N):
    # print the spaces
    for j in range(0, N-1-i):
        print(' ', end="")

    # print the stars
    for j in range(0, (2*i)+1):
        print('*', end="")

    # print the spaces
    for j in range(0, N-1-i):
        print(' ', end="")

    print("")

for i in range(0, 5):
    # print the spaces
    for j in range(0, i):
        print(' ', end="")

    # print the stars
    for j in range(0, 2*N-((2*i)+1)):
        print('*', end="")
    # print the spaces
    for j in range(0, i):
        print(' ', end="")

    if i != N-1:
        print()
