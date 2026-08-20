from array import array                                    

arr = array('i', [1, 2, 3, 4, 5])                                                     

print("Original array:", arr)

print("First element:", arr[0])

arr[1] = 10
print("After update:", arr)

arr.append(16)
print("After append:", arr)

arr.extend([17, 18])
print("After extend:", arr)

arr.insert(12, 35)
print("After insert:", arr)

arr.remove(35)
print("After remove:", arr)

arr.pop()
print("After pop:", arr)

print("Index of 4:", arr.index(4))
print("Count of 12:", arr.count(2))
print("Length:", len(arr))

arr.reverse()
print("After reverse:", arr)

print("Type code:", arr.typecode)

print("Array elements:")
for x in arr:
    print(x)

print("As list:", arr.tolist())
