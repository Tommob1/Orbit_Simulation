import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
G = 6.67430e-11  # Gravitational constant
m1 = 1.989e30    # Mass of the sun
m2 = 5.972e24    # Mass of the earth

# Initial positions and velocities
r1 = np.array([0.0, 0.0], dtype=float)         # Sun's initial position
r2 = np.array([1.496e11, 0.0], dtype=float)    # Earth's initial position
v1 = np.array([0.0, 0.0], dtype=float)         # Sun's initial velocity
v2 = np.array([0.0, 29780.0], dtype=float)     # Earth's initial velocity

# Time settings
dt = 60 * 60      # Time step in seconds (1 hour)
t_max = 365.25 * 24 * 60 * 60  # One year in seconds

# Lists to store positions
positions1 = []
positions2 = []

# Function to compute gravitational force
def compute_gravitational_force(r1, r2, m1, m2):
    r = r2 - r1
    distance = np.linalg.norm(r)
    force = G * m1 * m2 / distance**2
    force_vector = force * r / distance
    return force_vector

# Simulation loop
t = 0
while t < t_max:
    force_vector = compute_gravitational_force(r1, r2, m1, m2)

    # Update velocities
    v1 += force_vector / m1 * dt
    v2 -= force_vector / m2 * dt

    # Update positions
    r1 += v1 * dt
    r2 += v2 * dt

    # Store positions
    positions1.append(r1.copy())
    positions2.append(r2.copy())

    t += dt

positions1 = np.array(positions1)
positions2 = np.array(positions2)

# Plotting
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1.6e11, 1.6e11)
ax.set_ylim(-1.6e11, 1.6e11)

line1, = ax.plot([], [], lw=2, label='Body 1 Path', color='orange')
line2, = ax.plot([], [], lw=2, label='Body 2 Path', color='blue')
point1, = ax.plot([], [], 'o', color='orange', label='Body 1')
point2, = ax.plot([], [], 'o', color='blue', label='Body 2')

# Text annotations for telemetry data
telemetry_text1 = ax.text(0, 0, '', color='orange', ha='left', va='bottom')
telemetry_text2 = ax.text(0, 0, '', color='blue', ha='left', va='bottom')

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    point1.set_data([], [])
    point2.set_data([], [])
    telemetry_text1.set_text('')
    telemetry_text2.set_text('')
    return line1, line2, point1, point2, telemetry_text1, telemetry_text2

def animate(i):
    line1.set_data(positions1[:i, 0], positions1[:i, 1])
    line2.set_data(positions2[:i, 0], positions2[:i, 1])
    point1.set_data(positions1[i, 0], positions1[i, 1])
    point2.set_data(positions2[i, 0], positions2[i, 1])

    telemetry_text1.set_position((positions1[i, 0], positions1[i, 1]))
    telemetry_text1.set_text(
        f'Body 1 (Sun)\n({positions1[i, 0]:.2e}, {positions1[i, 1]:.2e})'
    )
    telemetry_text2.set_position((positions2[i, 0], positions2[i, 1]))
    telemetry_text2.set_text(
        f'Body 2 (Earth)\n({positions2[i, 0]:.2e}, {positions2[i, 1]:.2e})'
    )

    return line1, line2, point1, point2, telemetry_text1, telemetry_text2

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(positions1), interval=20, blit=True)

ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_title('Orbit Simulation')
ax.legend()
ax.grid()
ax.axis('equal')

plt.show()