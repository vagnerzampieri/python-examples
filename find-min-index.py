# Big O: O(n)
def find_min_index(arr):
    # 1. Set the min to the first element of the array
    min = arr[0]
    min_index = 0

    # 2. Loop through the array
    for i in range(1, len(arr)):
        # 3. Check if the current element is lower than the min
        if arr[i] < min:
            # 4. If so, set the min to the current element
            min = arr[i]
            # 5. Set the min_index to the current index
            min_index = i

    return min_index

print(find_min_index([7, 2, 3, 9, 4]))

print(find_min_index([7, 2, 3, -9, 4]))

print(find_min_index([7, 2, 3, 0, 4]))