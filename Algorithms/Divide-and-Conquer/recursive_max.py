def recursive_max(arr):
    # Base-case:1
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    else:
        # recursive call with smaller segment
        max_num = max(arr[1:])
        return arr[0] if arr[0] > max_num else max_num


print(recursive_max([2, 9, 3, 150]))
