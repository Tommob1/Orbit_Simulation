import numpy as np
import matplotlib.pyplot as plt

#Gravitational constant
G = 6.67430e-11

#Masses of the Sun and the Earth in KG (m1 = Sun, m2 = Earth)
m1 = 1.989e30
m2 = 5.972e24

#Initial positions (in meters)
r1 = np.array([0, 0])
r2 = np.array([1.496e11, 0])

#Initial velocities (m/s)
v1 = np.array([0, 0])
v2 = np.array([0, 29780])

#Time step
dt = 60 * 60

#Simulation duration
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

# Plot the orbits
plt.figure(figsize=(8, 8))
plt.plot(positions1[:, 0], positions1[:, 1], label='Body 1')
plt.plot(positions2[:, 0], positions2[:, 1], label='Body 2')
plt.scatter([positions1[0, 0]], [positions1[0, 1]], color='orange', label='Initial Position 1')
plt.scatter([positions2[0, 0]], [positions2[0, 1]], color='blue', label='Initial Position 2')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Orbit Simulation')
plt.legend()
plt.grid()
plt.axis('equal')
plt.show()