import numpy as np

# Given matrices
A = np.array([[3, 4], [7, 8]])
B = np.array([[5, 3], [2, 1]])

# 1. Prove A * A^-1 = I
A_inv = np.linalg.inv(A)
identity_result = np.dot(A, A_inv)

print("1. A * A^-1:")
print(identity_result)

# 2. Prove AB ≠ BA
AB = np.dot(A, B)
BA = np.dot(B, A)

print("\n2. AB:")
print(AB)

print("\nBA:")
print(BA)

print("\nAB != BA:", not np.array_equal(AB, BA))

# 3. Prove (AB)^T = B^T * A^T
left_side = np.transpose(AB)
right_side = np.dot(np.transpose(B), np.transpose(A))

print("\n3. (AB)^T:")
print(left_side)

print("\nB^T * A^T:")
print(right_side)

print("\nAre they equal:", np.array_equal(left_side, right_side))


# -------------------------------------------------
# Solve Linear Equations using Matrix Inverse Method
# -------------------------------------------------

# Equations:
# 2x − 3y + z = −1
# x − y + 2z = −3
# 3x + y − z = 9

# Matrix representation AX = B
A_matrix = np.array([
    [2, -3, 1],
    [1, -1, 2],
    [3, 1, -1]
])

B_matrix = np.array([
    [-1],
    [-3],
    [9]
])

# Find inverse of A
A_matrix_inv = np.linalg.inv(A_matrix)

# Solve X = A^-1 * B
X = np.dot(A_matrix_inv, B_matrix)

print("\nSolution of Linear Equations (x, y, z):")
print(X)