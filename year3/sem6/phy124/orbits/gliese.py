import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('gliese876ini.txt')
M = data[:, 0]  # Masses
R = data[:, 1:3]  # Positions
V = data[:, 3:]  # Velocities

# Number of bodies
N = data.shape[0]


dt = 900  
total_time = 130 * 24 * 3600  
num_steps = int(total_time / dt)

positions = np.zeros((N, num_steps, 2))

current_V = V.copy()
current_R = R.copy()

# Leapfrog integration
for i in range(num_steps):
    accelerations = np.zeros_like(current_R)
    for j in range(N):
        for k in range(N):
            if j != k:
                accelerations[j] += M[k] * (current_R[k] - current_R[j]) / np.linalg.norm(current_R[k] - current_R[j])**3

    # Half-step velocity update
    current_V += 0.5 * dt * accelerations
    
    # Full-step position update
    current_R += dt * current_V
    
    # Update accelerations with new positions
    new_accelerations = np.zeros_like(current_R)
    for j in range(N):
        for k in range(N): 
            if j != k: # Avoid dividing by zero
                 new_accelerations[j] += M[k] * (current_R[k] - current_R[j]) / np.linalg.norm(current_R[k] - current_R[j])**3

    # Complete velocity step
    current_V += 0.5 * dt * new_accelerations
    
    positions[:, i, :] = current_R

fig, ax = plt.subplots()
for i in range(N):
    ax.plot(positions[i, :, 0], positions[i, :, 1], label=f'Body {i+1}')
ax.set_aspect('equal')
ax.set_xlabel('X (light-seconds)')
ax.set_ylabel('Y (light-seconds)')
ax.set_title('Orbits in the Gliese 876 System')
ax.legend()
plt.show()