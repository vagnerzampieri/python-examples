# Big O: O(n)
def fat(x):
    # 1. Check if x is 0
    if x == 0:
        # 2. If so, return 1
        return 1
    else:
        # 3. If not, return x * fat(x-1)
        # 4. Call fat(x-1) recursively
        return x * fat(x-1)

print(fat(5))

print(fat(10))