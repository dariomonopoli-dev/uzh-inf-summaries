import numpy as np

input = [7, 5, 4, 2, 6, 5, 2, 2]


def FFT(x):
    N = len(x)
    H = N // 2

    if N == 1:
        return x
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(-1j * np.pi * np.arange(H) / H)

        X = np.concatenate([X_even + factor * X_odd, X_even - factor * X_odd])
        return X


print("Result: {:.6f}".format(FFT(input)[-1]))