# Big O: O(n)
def find_max_index(arr):
    # 1. Set the max to the first element of the array
    max = arr[0]
    # 2. Set the max_index to the first index of the array
    max_index = 0

    # 3. Loop through the array
    for i in range(1, len(arr)):
        # 4. Check if the current element is higher than the max
        if arr[i] > max:
            # 5. If so, set the max to the current element
            max = arr[i]
            # 6. Set the max_index to the current index
            max_index = i

    return max_index

print(find_max_index([7, 2, 3, 9, 4]))

print(find_max_index([7, 2, 3, -9, 4]))

print(find_max_index([7, 2, 3, 0, 4]))