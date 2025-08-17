import numpy as np
import matplotlib.pyplot as plt

gamma = 0.25
lambda_ = 0.075

# Initial conditions
phi_0 = 0.0
v_0 = 0.0
Omega = 1.0
dt = 0.01
total_time = 20  # total time for the simulation


def evolve_pendulum(phi_0, v_0, gamma, lambda_, dt, total_time):
    times = np.arange(0, total_time, dt)
    phi = phi_0
    v = v_0 - 0.5 * dt * (gamma * np.sin(phi_0) + lambda_ * np.sin(phi_0))
    phi_values = [phi_0]

    for tau in times[:-1]:  # we compute until the state before total_time (otherwise we would need to calculate another step, we avoid extending the computation beyong the intended simulation time)
        phi_half = phi + v * dt / 2  # Half-step position update
        v += (
            -gamma * np.sin(phi_half) - lambda_ * np.sin(phi_half - tau)
        ) * dt  # Full-step velocity update
        phi = phi_half + v * dt / 2  # Complete the position update
        phi_values.append(phi)

    return times, phi_values


times, phi_values = evolve_pendulum(phi_0, v_0, gamma, lambda_, dt, total_time)

plt.figure(figsize=(12, 6))
plt.plot(0.03 * np.sin(times) + 0.4*np.sin(phi_values), -0.03*np.cos(times) - 0.4*np.cos(phi_values), label="Pendulum Angle")
plt.title("Time Evolution of Pendulum on a Wheel")
plt.xlabel("Time units")
plt.ylabel("Angle (radians)")
plt.legend()
plt.grid(True)
plt.show()
