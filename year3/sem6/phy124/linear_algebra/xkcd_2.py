import numpy as np

N = 10

Rinv = np.zeros((N * N, N * N))
b = np.zeros((N * N, 1))
b[int(N / 2)] = 1
b[int(N / 2 + N - 2)] = -1

for i in range(N):
    for j in range(N):
        total = 0
        if i != 0:
            Rinv[i * N + j][(i - 1) * N + j] = -1
            total += 1
        if j != 0:
            Rinv[i * N + j][i * N + j - 1] = -1
            total += 1
        if i != N - 1:
            Rinv[i * N + j][(i + 1) * N + j] = -1
            total += 1
        if j != N - 1:
            Rinv[i * N + j][i * N + j + 1] = -1
            total += 1
        Rinv[i * N + j][i * N + j] = total

result = np.linalg.solve(Rinv, b)
print(result[int(N / 2)] - result[int(N / 2) + N - 2])