import numpy as np
from scipy.integrate import odeint

def projectile_derivatives(y, t):
    x, y_pos, vx, vy = y 
    g = 9.81  # gravity constant
    # The position derivatives $\frac{d x}{d t}$ and $\frac{d y}{d t}$ are the components of velocity $v_x$ and $v_y$. The velocity derivative $\frac{d v_x}{d t}$ is $O$ (no horizontal acceleration).
    # The velocity derivative $\frac{d v_y}{d t}$ is $-g$ (only gravity acts vertically). 
    # Derivatives: [dx/dt, dy/dt, dvx/dt, dvy/dt]
    derivatives = [vx, vy, 0, -g]
    return derivatives

def leapfrog_parabolic_throw_odeint(vx0, vy0, t_end=1.1, dt=0.1):
    t = np.linspace(0, t_end, 100)  
    initial_conditions = [0.0, 0.0, vx0, vy0]  
    
    result = odeint(projectile_derivatives, initial_conditions, t)
    
    x_final, y_final = result[-1, 0], result[-1, 1]
    
    return f"{x_final:.3f},{y_final:.3f}"

vx0 = 14.0
vy0 = 14.0

print(leapfrog_parabolic_throw_odeint(vx0, vy0))
