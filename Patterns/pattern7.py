'''
    *
   *** 
  *****
 *******
*********
'''
N = 9
for i in range(0, N):
    # print 'spaces'
    for j in range(1, N-i):
        print(' ', end="")
    # print 'stars'
    for j in range(0, 2*i+1):
        print('*', end="")
    # print 'spaces'
    for j in range(1, N-i):
        print(' ', end="")
    if i is not N-1:
        print()
