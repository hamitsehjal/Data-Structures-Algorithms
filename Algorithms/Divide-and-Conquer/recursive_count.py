def count(my_list):
    if my_list == []:
        return 0
    return 1 + count(my_list[1:])


my_list = [2, 6, 5]

print(count(my_list))
