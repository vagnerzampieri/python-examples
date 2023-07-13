def quicksort(array):
    # 1. Check if the array is empty or has one element
    if len(array) < 2:
        return array
    else:
        # 2. If so, set the pivot to the first element of the array
        pivot = array[0]
        print(f'pivot {pivot}')
        # 3. Set the less array to the elements of the array that are lower than the pivot
        less = [i for i in array[1:] if i <= pivot]
        print(f'less {less}')
        # 4. Set the greater array to the elements of the array that are greater than the pivot
        greater = [i for i in array[1:] if i > pivot]
        print(f'greater {greater}')
        # 5. Return the quicksort of the less array + the pivot + the quicksort of the greater array
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))

print(quicksort([10, 5, 2, 3, 1, 4, 6, 7, 8, 9]))

print(quicksort([10, 8, 2, 3, 1, 4, 5, 7, 6, 9]))
