import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, fftshift


def fourier(f):
    """ fourier transform """
    return fftshift(fft(fftshift(f)))


def ifourier(f):
    """ inverse fourier transform """
    return fftshift(ifft(fftshift(f)))


N = 100
x = (np.arange(N) - N // 2) * 2 * np.pi / N
k = (np.arange(N) - N // 2) * 2 * np.pi / N


def V(x):
    return 1 / 2 * x ** 2


def Wave(x):
    #return x*np.exp(-(x ** 2 / 2))
    #return np.sin(3*x) + np.cos(1.5*x)
    return np.exp(-(x ** 2 / 2))


def algorithm(start):
    results = [start]
    result_roof = []
    result_noroof = []

    dt = 0.5
    for t in range(50):
        results.append(fourier(results[-1]))
        results.append(results[-1] * np.exp(-1j * k ** 2 * dt / 4))
        results.append(ifourier(results[-1]))
        results.append(results[-1] * np.exp(-1j * V(x) * dt))
        results.append(fourier(results[-1]))
        results.append(results[-1] * np.exp(-1j * k ** 2 * dt / 4))
        result_roof.append(results[-1])
        results.append(ifourier(results[-1]))
        result_noroof.append(results[-1])
    return result_roof, result_noroof


roof, noroof = algorithm(Wave(x))

plt.figure()
for i, j in zip(noroof, roof):
    plt.subplot(211)
    plt.plot(x, i.real)
    plt.xlim(-np.pi, np.pi)
    plt.ylim(-1.5, 1.5)
    plt.subplot(212)
    plt.plot(x, j.real)
    plt.xlim(-np.pi, np.pi)
    plt.ylim(-13, 13)
    plt.pause(0.25)
    plt.clf()