import numpy as np

# Given arrays
x = np.array([[1, 2], [3, 5]])
y = np.array([[5, 6], [7, 8]])

v = np.array([9, 10])
w = np.array([11, 12])

# 1. Add the two arrays
print("1. Addition of x and y:")
print(x + y)

# 2. Subtract the two arrays
print("\n2. Subtraction of x and y:")
print(x - y)

# 3. Multiply the array with any integer (example: 2)
print("\n3. Multiply x with 2:")
print(x * 2)

# 4. Square of each element
print("\n4. Square of elements in x:")
print(np.square(x))

# 5. Dot products
print("\n5. Dot Products:")
print("v . w =", np.dot(v, w))
print("x . v =", np.dot(x, v))
print("x . y =")
print(np.dot(x, y))

# 6. Concatenation
print("\n6. Concatenate x and y along rows:")
print(np.concatenate((x, y), axis=0))  # or np.vstack((x, y))

print("\nConcatenate v and w along columns:")
print(np.vstack((v, w)).T)

# 7. Concatenate x and v
print("\n7. Attempt to concatenate x and v:")
try:
    print(np.concatenate((x, v)))
except ValueError as e:
    print("Error:", e)
    print("Explanation: x is a 2D array (2x2) while v is a 1D array, so their dimensions do not match for concatenation.")