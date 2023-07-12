class Box:
    def __init__(self, content):
        self.content = content

    def box(self):
        return self.content == 'box'

    def key(self):
        return self.content == 'key'

array = [Box('box'), Box('box'), Box('box'), Box('key'), Box('box')]

# Big O: O(n)
def open_box(arr):
    # 1. Loop through the array
    for i in range(len(arr)):
        # 2. Check if the current element is a key
        if arr[i].key():
            return "You found the key!"
        # 3. Check if the current element is a box
        elif arr[i].box():
            # 4. If so, open the box
            # 5. Pass the rest of the array to the function
            return open_box(arr[i+1:])
    # 6. If not, return a message
    return "You didn't find the key."

print(open_box(array))
