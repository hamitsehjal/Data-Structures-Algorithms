'''
*********
 *******
  *****
   ***
    *
'''
# N = 5
# m = 0
# for i in range(N-1, -1, -1):
#     # print the spaces
#     for j in range(0, m):
#         print(' ', end="")

#     # print the '*'
#     for j in range(0, (i*2)+1):
#         print('*', end="")

#     # print the spaces
#     for j in range(0, m):
#         print(' ', end="")

#     m = m+1
#     if m is not N:
#         print()

N = 5

for i in range(0, 5):
    # print the spaces
    for j in range(0, i):
        print(' ', end="")

    # print the stars
    for j in range(0, 2*N-(2*i+1)):
        print('*', end="")
    # print the spaces
    for j in range(0, i):
        print(' ', end="")

    if i != N-1:
        print()
