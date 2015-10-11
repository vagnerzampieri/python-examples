elements = []

if not elements:
    elements.append(1)
elif elements.itemsize == 1:
    elements.append(2)
else:
    print("Element")

for element in elements:
    print("Element %d" % element)
