'''
Printing 5 stars on each line 5 times
*****
*****
*****
*****
*****
'''
for i in range(0, 5):
    for j in range(0, 5):
        print('*', end="")
    print()

# Python'print function automatically add a new line followed by content.
# To surpass this action, you can use 'end' parameter of the print function
# and set it to empty string
