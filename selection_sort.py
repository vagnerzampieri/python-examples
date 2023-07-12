from find_min_index import find_min_index

# Big O: O(n)
def selection_sort(arr):
    # 1. Create a new array
    newArr = []
    # 2. Loop through the array
    for i in range(len(arr)):
        # 3. Find the min index of the array
        min = find_min_index(arr)
        # 4. Pop the min index from the array and append it to the new array
        newArr.append(arr.pop(min))

    return newArr

print(selection_sort([5, 3, 6, 2, 10]))

print(selection_sort([5, 3, 6, 2, 10, -1, 0, 4]))

print(selection_sort([5, 3, 6, 2, 10, -1, 0, 4, 1]))
