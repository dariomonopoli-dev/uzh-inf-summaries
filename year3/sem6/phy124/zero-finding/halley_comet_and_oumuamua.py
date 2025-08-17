import numpy as np
import matplotlib.pyplot as plt

# Constants for Halley's Comet
e_halley = 0.967
a_halley = 17.8

# Constants for 'Oumuamua
e_oumuamua = 1.20
a_oumuamua = 1.28


def kepler_halley(psi, t):
    return psi - e_halley * np.sin(psi) - t


def derivative_kepler_halley(psi):  # derive on psi
    return 1 - e_halley * np.cos(psi)


def kepler_oumuamua(psi, t):
    return e_oumuamua * np.sinh(psi) - psi - t


def derivative_kepler_oumuamua(psi):  # derive on psi
    return e_oumuamua * np.cosh(psi) - 1


def newton_raphson_root(f, f_prime, t, psi_initial, tol=1e-6, max_iter=100):
    psi = psi_initial
    for i in range(max_iter):
        f_val = f(psi, t)
        f_prime_val = f_prime(psi)
        next_psi = psi - f_val / f_prime_val
        if abs(next_psi - psi) < tol:
            return next_psi
        psi = next_psi
    return psi


t_values = np.linspace(0, 2*np.pi, 5000)
x_halley, y_halley = [], []
x_oumuamua, y_oumuamua = [], []
psi_previous = 0 

# Calculate orbit for Halley's Comet
for t in t_values:
    psi = newton_raphson_root(kepler_halley, derivative_kepler_halley, t, psi_previous)
    psi_previous = psi  
    x_h = a_halley * (np.cos(psi) - e_halley)
    y_h = a_halley * np.sqrt(1 - e_halley**2) * np.sin(psi)
    x_halley.append(x_h)
    y_halley.append(y_h)

# Calculate orbit for 'Oumuamua
t_values_oumuamua = np.linspace(-np.pi, np.pi, 400)
for t in t_values_oumuamua:
    psi = newton_raphson_root(
        kepler_oumuamua, derivative_kepler_oumuamua, t, psi_initial=1.0
    )
    x_o = a_oumuamua * (e_oumuamua - np.cosh(psi))
    y_o = a_oumuamua * np.sqrt(e_oumuamua**2 - 1) * np.sinh(psi)
    x_oumuamua.append(x_o)
    y_oumuamua.append(y_o)


plt.figure(figsize=(10, 5))
plt.plot(x_halley, y_halley, label="Halley's Comet")
plt.plot(x_oumuamua, y_oumuamua, label="'Oumuamua")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Orbits of Halley's Comet and 'Oumuamua")
plt.legend()
plt.grid(True)
plt.show()