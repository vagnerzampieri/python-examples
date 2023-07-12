def binary_search(list, item):
    # 1. Set the low and high to the first and last index of the list
    count_attempts = 0
    low = 0
    high = len(list) - 1

    while low <= high:
        # 2. Find the middle element
        count_attempts += 1
        mid = int((low + high) / 2)
        guess = list[mid]

        # 3. Check if the middle element is the item we are looking for
        if guess == item:
            return [mid, count_attempts]

        # 4. If not, check if the item is higher or lower than the middle element
        if guess > item:
            # 5. If lower, set the high to the middle element - 1
            high = mid - 1

        else:
            # 6. If higher, set the low to the middle element + 1
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))

print(binary_search(my_list, -1))

my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print(binary_search(my_list, 11))