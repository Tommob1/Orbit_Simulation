import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Gravitational constant
G = 6.67430e-11

# Masses of the Sun and the Earth in KG (m1 = Sun, m2 = Earth)
m1 = 1.989e30
m2 = 5.972e24

# Initial positions (in meters)
r1 = np.array([0.0, 0.0], dtype=float)
r2 = np.array([1.496e11, 0.0], dtype=float)

# Initial velocities (m/s)
v1 = np.array([0.0, 0.0], dtype=float)
v2 = np.array([0.0, 29780.0], dtype=float)

# Time step
dt = 60 * 60 * 60

# Simulation duration
t_max = 365.25 * 24 * 60 * 60

positions1 = []
positions2 = []

t = 0

while t < t_max:
    # Calculate the distance vector
    r = r2 - r1
    distance = np.linalg.norm(r)

    # Calculate the force
    force = G * m1 * m2 / distance**2
    force_vector = force * r / distance

    # Update velocities
    v1 += force_vector / m1 * dt
    v2 -= force_vector / m2 * dt

    # Update positions
    r1 += v1 * dt
    r2 += v2 * dt

    # Store positions
    positions1.append(r1.copy())
    positions2.append(r2.copy())

    # Update time
    t += dt

# Convert position lists to numpy arrays for plotting
positions1 = np.array(positions1)
positions2 = np.array(positions2)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1.6e11, 1.6e11)
ax.set_ylim(-1.6e11, 1.6e11)

# Initialize the plot elements we want to animate
line1, = ax.plot([], [], lw=2, label='Body 1 Path')
line2, = ax.plot([], [], lw=2, label='Body 2 Path')
point1, = ax.plot([], [], 'o', color='orange', label='Body 1')
point2, = ax.plot([], [], 'o', color='blue', label='Body 2')

# Initialize function
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    point1.set_data([], [])
    point2.set_data([], [])
    return line1, line2, point1, point2

# Animation function
def animate(i):
    line1.set_data(positions1[:i, 0], positions1[:i, 1])
    line2.set_data(positions2[:i, 0], positions2[:i, 1])
    point1.set_data(positions1[i, 0], positions1[i, 1])
    point2.set_data(positions2[i, 0], positions2[i, 1])
    return line1, line2, point1, point2

# Call the animator
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(positions1), interval=20, blit=True)

# Plot the orbits
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_title('Orbit Simulation')
ax.legend()
ax.grid()
ax.axis('equal')

plt.show()