# Big O: O(n)
def recursion_sum(array):
    # 1. Check if the array is empty
    if len(array) == 0:
        # 2. If so, return 0
        return 0
    # 3. If not, return the first element of the array + recursion_sum(rest of the array)
    return array[0] + recursion_sum(array[1:])

print(recursion_sum([1, 2, 3, 4, 5]))

print(recursion_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))