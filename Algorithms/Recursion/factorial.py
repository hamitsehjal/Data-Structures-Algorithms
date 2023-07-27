
""" Recursion example through concept of getting factorial of any number"""


def get_factorial(num):
    '''
        Calculates and returns factorial of `num`
    '''

    if num == 1:
        return 1

    return num*get_factorial(num-1)


print(get_factorial(8))


def factorial_iterative(num):
    """Iteratively calculates the factorial."""
    result = 1  # initialize a variable to store final answer.
    while num > 1:
        result = result*num
        num = num-1

    return result


print(factorial_iterative(8))
