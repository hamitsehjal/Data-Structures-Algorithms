
def sum(numbers):
    """
    Implementation in terms of code is easy and breif
    but flow of control is a bit complex
    """

    # stopping condition for recursion
    if len(numbers)<=0:
        return 0

    # recursive pattern
    print("Before Call: %s" % numbers)
    remaining_numbers=sum(numbers[1:])
    print("Call to Sum: %s --> %d + %s" %(numbers, numbers[0], remaining_numbers))
    return numbers[0]+remaining_numbers


alist=[1,3,45,5]
# print("Before Sum: ",alist)
print("After Sum: ", sum(alist))