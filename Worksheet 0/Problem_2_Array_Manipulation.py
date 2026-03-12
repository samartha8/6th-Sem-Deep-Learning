import numpy as np

# 1. Create an array with values ranging from 10 to 49
arr1 = np.arange(10, 50)
print("1. Array from 10 to 49:")
print(arr1)

# 2. Create a 3x3 matrix with values ranging from 0 to 8
arr2 = np.arange(9).reshape(3, 3)
print("\n2. 3x3 matrix from 0 to 8:")
print(arr2)

# 3. Create a 3x3 identity matrix
arr3 = np.eye(3)
print("\n3. 3x3 Identity matrix:")
print(arr3)

# 4. Create a random array of size 30 and find the mean
arr4 = np.random.random(30)
print("\n4. Random array of size 30:")
print(arr4)
print("Mean:", arr4.mean())

# 5. Create a 10x10 array with random values and find min and max
arr5 = np.random.random((10, 10))
print("\n5. 10x10 random array:")
print(arr5)
print("Minimum:", arr5.min())
print("Maximum:", arr5.max())

# 6. Create a zero array of size 10 and replace 5th element with 1
arr6 = np.zeros(10)
arr6[4] = 1
print("\n6. Zero array with 5th element replaced by 1:")
print(arr6)

# 7. Reverse an array
arr7 = np.array([1, 2, 0, 0, 4, 0])
reversed_arr = arr7[::-1]
print("\n7. Reversed array:")
print(reversed_arr)

# 8. Create a 2D array with 1 on border and 0 inside
arr8 = np.ones((5, 5))
arr8[1:-1, 1:-1] = 0
print("\n8. 2D array with border 1 and inside 0:")
print(arr8)

# 9. Create an 8x8 checkerboard matrix
arr9 = np.zeros((8, 8), dtype=int)
arr9[1::2, ::2] = 1
arr9[::2, 1::2] = 1
print("\n9. 8x8 Checkerboard pattern:")
print(arr9)