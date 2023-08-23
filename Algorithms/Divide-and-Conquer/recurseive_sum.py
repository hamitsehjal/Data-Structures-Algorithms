def recursive_sum(arr):
    # Base case: if an empty array, return 0
    if len(arr)==0:
        return 0
    else:
        total=arr[0]+sum(arr[1:])
     return total