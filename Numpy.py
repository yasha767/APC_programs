# 1 one-dimensional array
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Array:", arr)
print("Size:", arr.size)
print("Data type:", arr.dtype)
print("Number of dimensions:", arr.ndim)


# 2 arithmetic operations on two arrays
a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)


# 3 maximum, minimum, sum and average
arr = np.array([10, 25, 15, 40, 35, 50, 5, 30, 45, 20])

print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))


# 4 separate even and odd numbers
arr = np.arange(1, 21)

print("Even numbers:", arr[arr % 2 == 0])
print("Odd numbers:", arr[arr % 2 != 0])


# 5 reshape array into different matrices
arr = np.arange(1, 13)

print("2 x 6 matrix:")
print(arr.reshape(2, 6))

print("3 x 4 matrix:")
print(arr.reshape(3, 4))

print("4 x 3 matrix:")
print(arr.reshape(4, 3))


# 6 matrix addition
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

b = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("Matrix Addition:")
print(a + b)


# 7 matrix multiplication
a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print("Matrix Multiplication:")
print(np.dot(a, b))


# 8 transpose of a matrix
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print("Original Matrix:")
print(arr)

print("Transpose:")
print(arr.T)


# 9 access rows, columns and diagonal elements
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print("First row:", arr[0])
print("Last column:", arr[:, -1])
print("Diagonal elements:", np.diag(arr))
print("Second and third rows:")
print(arr[1:3])


# 10 sum of each row and column
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print("Sum of each row:", np.sum(arr, axis=1))
print("Sum of each column:", np.sum(arr, axis=0))


# 11 slicing an array
arr = np.arange(1, 21)

print("First 5 elements:", arr[:5])
print("Last 5 elements:", arr[-5:])
print("Alternate elements:", arr[::2])
print("Reverse order:", arr[::-1])


# 12 replace elements greater than 50
arr = np.array([10, 25, 55, 70, 40, 80, 35, 90, 45, 60])

arr[arr > 50] = 0

print("Modified array:", arr)


# 13 ascending and descending order
arr = np.array([50, 10, 80, 30, 70, 20, 90, 40])

print(" Ascending order:", np.sort(arr))
print("Descending order:", np.sort(arr)[::-1])


# 14 unique elements
arr = np.array([10, 20, 10, 30, 40, 20, 50, 30, 60, 40])

print("Unique elements:", np.unique(arr))


# 15 concatenate arrays horizontally and vertically
a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print("Horizontal concatenation:")
print(np.hstack((a, b)))

print("Vertical concatenation:")
print(np.vstack((a, b)))


# 16 calculate marks statistics
marks = np.array([75, 82, 68, 90, 55, 78, 88, 92, 70, 85])

print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))
print("Average marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard deviation:", np.std(marks))


# 17 students scoring above average
marks = np.array([45, 67, 89, 72, 56, 91, 38, 76, 84, 63,
                  95, 52, 69, 81, 47, 73, 88, 59, 77, 65])

average = np.mean(marks)

print("Class average:", average)
print("Marks above average:", marks[marks > average])


# 18 create and display a 3D array
arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)
print("Number of dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)


# 19 access elements of a 3D array
arr = np.arange(1, 25).reshape(2, 3, 4)

print("First element:", arr[0, 0, 0])
print("Last element:", arr[-1, -1, -1])
print("Element at [0,1,2]:", arr[0, 1, 2])
print("Element at [1,2,3]:", arr[1, 2, 3])


# 20 Sum of elements in a 3D array
arr = np.arange(1, 25).reshape(2, 3, 4)

print("Sum of all elements:", np.sum(arr))
print("Sum of each layer:", np.sum(arr, axis=(1, 2)))
print("Sum along rows:")
print(np.sum(arr, axis=2))
print("Sum along columns:")
print(np.sum(arr, axis=1))


# 21 Replace values greater than 50 with 0
np.random.seed(1)

arr = np.random.randint(1, 101, size=(2, 3, 4))

print("Original array:")
print(arr)

arr[arr > 50] = 0

print("Modified array:")
print(arr)


# 22 Statistics of a random 3D array
np.random.seed(1)

arr = np.random.randint(1, 101, size=(3, 4, 5))

print("Array:")
print(arr)

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))


# 23 Flatten a 3D array
arr = np.arange(1, 25).reshape(2, 3, 4)

print("Original 3D array:")
print(arr)

print("Flattened array:")
print(arr.flatten())


# 24 Flatten array and calculate statistics
arr = np.arange(1, 28).reshape(3, 3, 3)

flat = arr.flatten()

print("Flattened array:")
print(flat)

print("Sum:", np.sum(flat))
print("Average:", np.mean(flat))
print("Maximum:", np.max(flat))
print("Minimum:", np.min(flat))


# 25 Filter elements of a random 3D array
np.random.seed(1)

arr = np.random.randint(1, 101, size=(3, 4, 5))

flat = arr.flatten()
average = np.mean(flat)

print("Original array:")
print(arr)

print("Elements greater than 50:")
print(flat[flat > 50])

print("Even numbers:")
print(flat[flat % 2 == 0])

print("Elements less than average:")
print(flat[flat < average])
