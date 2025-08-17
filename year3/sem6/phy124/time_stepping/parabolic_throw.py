def leapfrog_parabolic_throw(vx0, vy0, t_end=4.5, dt=0.1):
    g = 9.81

    x = 0.0
    y = 0.0
    vx = vx0
    vy = vy0
    t = 0.0

    while (
        t < t_end
    ):  # continue to update the velocity and position until the time reaches or exceeds the end time

        # This step moves the position $\vec{r}$ (comprising $x$ and $y$ ) halfway forward in time, using the current velocity $\vec{v}$ (comprising $v_x$ and $v_y$ ). It's a "half-step" because it only accounts for half of the time interval delta_t.
        x += vx * dt / 2
        y += vy * dt / 2

        vy -= (
            g * dt
        )  # Full step: update the velocity in the y direction, only vertical velocity changes due to gravity

        x += (
            vx * dt / 2
        )  # half step again: update the position in the x direction with the new velocity
        y += vy * dt / 2

        t += dt  # update the time

    return f"{x:.3f},{y:.3f}"  # Return the final position of the projectile, rounded to three decimal places


vx0 = 13.0
vy0 = 13.0

result = leapfrog_parabolic_throw(vx0, vy0)
print(result)
