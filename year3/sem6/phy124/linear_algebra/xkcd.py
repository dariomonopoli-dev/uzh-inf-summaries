import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

def initialize_matrix(N):
    A = lil_matrix((N**2, N**2)) # list of lists format
    for y in range(N):
        for x in range(N):
            index = y * N + x
            # Periodic boundary conditions (modulo N is used to wrap around the edges of the grid)
            left = y * N + (x - 1) % N  # Wraps around horizontally
            right = y * N + (x + 1) % N
            up = ((y - 1) % N) * N + x  # Wraps around vertically
            down = ((y + 1) % N) * N + x


            # Set connections (connect each node to its four immediate neighbors (up, down, left, right))
            A[index, left] = -1 # -1 represents a connection between the central node and the left node
            A[index, right] = -1
            A[index, up] = -1
            A[index, down] = -1

            # Central node (sum of negative connections). Kirchhoff's current law: total current entering a node must be equal to the total current leaving it
            A[index, index] = 4

    return A

def solve_resistor_network(N):
    A = initialize_matrix(N)
    b = np.zeros(N**2)
    b[0] = 1  # Apply a unit 'voltage' at one corner
    x = spsolve(A, b) # better than np.linalg.solve for sparse matrices (most entries are zero)
    return x.reshape(N, N) # reshape the solution to a 2D grid with N rows and N columns (N is the number of nodes in one side of the grid)

# 10x10 grid example
N = 10
print(solve_resistor_network(N))
