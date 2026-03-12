import numpy as np

# 1. Initialize an empty array with size 2x2
empty_array = np.empty((2, 2))
print("1. Empty 2x2 array:")
print(empty_array)

# 2. Initialize an all one array with size 4x2
ones_array = np.ones((4, 2))
print("\n2. Ones array (4x2):")
print(ones_array)

# 3. Return a new array of given shape and type, filled with fill value
full_array = np.full((3, 3), 7)
print("\n3. Full array (3x3 filled with 7):")
print(full_array)

# 4. Return a new array of zeros with same shape and type as a given array
zeros_like_array = np.zeros_like(full_array)
print("\n4. Zeros like array:")
print(zeros_like_array)

# 5. Return a new array of ones with same shape and type as a given array
ones_like_array = np.ones_like(full_array)
print("\n5. Ones like array:")
print(ones_like_array)

# 6. Convert an existing list to a NumPy array
new_list = [1, 2, 3, 4]
numpy_array = np.array(new_list)
print("\n6. List converted to NumPy array:")
print(numpy_array)