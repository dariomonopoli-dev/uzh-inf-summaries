import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def hamiltonian_derivatives(t, y):
    r, phi, p_r, p_phi = y
    dr_dt = (1 - 2 / r) * p_r
    dphi_dt = p_phi / r**2
    dp_r_dt = -p_r**2 / r**2 + p_phi**2/r**3 - 1/(r-2)**2
    dp_phi_dt = 0
    return [dr_dt, dphi_dt, dp_r_dt, dp_phi_dt]

# Initial conditions
r_init = 135  # Initial radius > 6
phi_init = 0
p_r_init = 0
p_phi_init = 136.00796 # Initial angular momentum

# Time span and points
t_span = (0, 9855)  # Ending time matches given t for checking the program
t_eval = np.linspace(0, 9855, 300)  # For plotting

# Solve ODE
sol = solve_ivp(hamiltonian_derivatives, t_span, [r_init, phi_init, p_r_init, p_phi_init], t_eval=t_eval)

# Plot the orbit in polar coordinates
r = sol.y[0]
phi = sol.y[1]

x = phi - np.arccos(r_init / r)
y = r * np.sin(phi)

plt.figure()
plt.plot(t_eval, phi - np.arccos(r_init / r))
plt.xlabel("x (light-seconds)")
plt.ylabel("y (light-seconds)")
plt.title("Orbit in the Schwarzschild Metric")
plt.show()

# Print the final value of phi
print("Final value of phi:", phi[-1])
