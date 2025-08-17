import numpy as np

A = np.array([
    [2, -1, -1, 0],
    [-1, 3, -1, -1],
    [-1, -1, 3, -1],
    [0, -1, -1, 2]
])

b = np.array([1, 0, 0, -1])

V = np.linalg.solve(A, b)

V0, V3 = V[0], V[3]

difference = V0 - V3

print("Solution vector V:", V)
print("V0 - V3 =", difference)
