"""import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Given data (planetName, massEarth, distanceAU, radiusEarthRadii, rotationalPeriodDays, orbitalPeriodYears, eccentricity)
data = [
    ["Mars", 0.107, 1.523, 0.53, 1.03, 1.88, 0.09],
    ["Venus", 0.815, 0.723, 0.95, 243.02, 0.62, 0.01],
    ["Mercury", 0.055, 0.387, 0.38, 58.65, 0.24, 0.21],
    ["Earth", 1, 1, 1, 1, 1, 0.02],
]

# Function to generate points for the elliptical orbit with left focus at a given point
def generateEllipsePoints(centerX, centerY, semiMajorAxis, eccentricity, numPoints=1000):
    theta = np.linspace(0, 2 * np.pi, numPoints)
    c = semiMajorAxis * eccentricity
    a = semiMajorAxis
    b = a * np.sqrt(1 - eccentricity**2)
    x = centerX + c + a * np.cos(theta)
    y = centerY + b * np.sin(theta)
    return x, y

# Create the plot
fig, ax = plt.subplots()

# Plot the center point
center = ax.scatter(0, 0, s=200, color='orange', marker='o', label='Center')

# Plot the elliptical orbits with center at the sun
orbits = []
for planet in data:
    semiMajorAxis = planet[2]
    eccentricity = planet[6]

    x, y = generateEllipsePoints(0, 0, semiMajorAxis, eccentricity)
    orbit, = ax.plot(x, y, label=planet[0])
    orbits.append(orbit)

# Create spherical objects for each planet
planetObjs = [ax.plot([], [], 'o', markersize=10)[0] for _ in data]

# Set aspect ratio to 'equal' to ensure the plot shows circles as circles (ellipses as ellipses)
ax.set_aspect('equal')

# Add labels and title
plt.xlabel('X (AU)')
plt.ylabel('Y (AU)')
plt.title('Nested Elliptical Orbits')

# Individual time factors for each orbit's motion
orbitSpeed = [20.11, 60.97, 157.5, 37.8]

# Function to update the animation
def update(frame):
    # Calculate the position of the center (Sun) on its orbit around the center
    sunX = np.cos(2 * np.pi * frame / 100)  # Orbiting at 1 AU radius
    sunY = np.sin(2 * np.pi * frame / 100)  # Orbiting at 1 AU radius

    center.set_offsets((sunX, sunY))

    for i, planet in enumerate(data):
        semiMajorAxis = planet[2]
        eccentricity = planet[6]

        # Generate points for the orbit around the center
        x, y = generateEllipsePoints(sunX, sunY, semiMajorAxis, eccentricity)

        # Calculate the position of the planet on the orbit using the time factor
        planetX = x[int(frame * orbitSpeed[i]) % len(x)]
        planetY = y[int(frame * orbitSpeed[i]) % len(y)]

        planetObjs[i].set_xdata(planetX)
        planetObjs[i].set_ydata(planetY)

    return planetObjs + [center]

# Create the animation
ani = FuncAnimation(fig, update, frames=range(315), interval=(1000/30), blit=True)

# Show the plot
plt.grid(True)
plt.legend()
plt.show()"""





"""import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Given data (planetName, massEarth, distanceAU, radiusEarthRadii, rotationalPeriodDays, orbitalPeriodYears, eccentricity)
data = [
    ["Mars", 0.107, 1.523, 0.53, 1.03, 1.88, 0.09],
    ["Venus", 0.815, 0.723, 0.95, 243.02, 0.62, 0.01],
    ["Mercury", 0.055, 0.387, 0.38, 58.65, 0.24, 0.21],
]

# Function to generate points for the elliptical orbit with left focus at a given point
def generateEllipsePoints(centerX, centerY, semiMajorAxis, eccentricity, numPoints=1000):
    theta = np.linspace(0, 2 * np.pi, numPoints)
    c = semiMajorAxis * eccentricity
    a = semiMajorAxis
    b = a * np.sqrt(1 - eccentricity**2)
    x = centerX + c + a * np.cos(theta)
    y = centerY + b * np.sin(theta)
    return x, y

# Create the plot
fig, ax = plt.subplots()

# Plot the center point
center = ax.scatter(0, 0, s=200, color='orange', marker='o', label='Sun')

# Plot the elliptical orbits with center at the sun
orbits = []
for planet in data:
    semiMajorAxis = planet[2]
    eccentricity = planet[6]

    x, y = generateEllipsePoints(0, 0, semiMajorAxis, eccentricity)
    orbit, = ax.plot(x, y, label=planet[0], alpha=0.1)  # Adding transparency to create the trail effect
    orbits.append(orbit)

# Create lines for planet trails
planetTrails = [ax.plot([], [], '-', linewidth=1, alpha=0.5)[0] for _ in data]

# Create spherical objects for each planet
planetObjs = [ax.plot([], [], 'o', markersize=10)[0] for _ in data]

# Set aspect ratio to 'equal' to ensure the plot shows circles as circles (ellipses as ellipses)
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
# Add labels and title
plt.xlabel('X (AU)')
plt.ylabel('Y (AU)')
plt.title('Nested Elliptical Orbits with Line Trails')

# Individual time factors for each orbit's motion
orbitSpeed = [20.11, 60.97, 157.5, 37.8]
#orbitSpeed = [2.011, 6.097, 15.75, 3.78]
# Number of frames for the planet trails
trail_length = 1000
trail_x = np.zeros((len(data), trail_length))
trail_y = np.zeros((len(data), trail_length))

# Function to update the animation
def update(frame):
    # Calculate the position of the center (Sun) on its orbit around the center
    sunX = np.cos(2 * np.pi * frame / 100)  # Orbiting at 1 AU radius
    sunY = np.sin(2 * np.pi * frame / 100)  # Orbiting at 1 AU radius

    center.set_offsets((sunX, sunY))

    for i, planet in enumerate(data):
        semiMajorAxis = planet[2]
        eccentricity = planet[6]

        # Generate points for the orbit around the center
        x, y = generateEllipsePoints(sunX, sunY, semiMajorAxis, eccentricity)

        # Calculate the position of the planet on the orbit using the time factor
        planetX = x[int(frame * orbitSpeed[i]) % len(x)]
        planetY = y[int(frame * orbitSpeed[i]) % len(y)]

        planetObjs[i].set_xdata(planetX)
        planetObjs[i].set_ydata(planetY)

        # Update planet trails
        trail_x[i, frame % trail_length] = planetX
        trail_y[i, frame % trail_length] = planetY

        planetTrails[i].set_data(trail_x[i], trail_y[i])

    return planetObjs + planetTrails + [center]

# Create the animation
ani = FuncAnimation(fig, update, frames=range(1000), interval=(1000/300), blit=True)

# Show the plot
plt.grid(True)
plt.legend()
plt.show()"""


import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from matplotlib.animation import FuncAnimation

# Given data (planetName, massEarth, distanceAU, radiusEarthRadii, rotationalPeriodDays, orbitalPeriodYears, eccentricity)
data = [
    ["Mars", 0.107, 1.523, 0.53, 1.03, 1.88, 0.09],
    ["Venus", 0.815, 0.723, 0.95, 243.02, 0.62, 0.01],
    ["Mercury", 0.055, 0.387, 0.38, 58.65, 0.24, 0.21],
]

# Function to generate points for the elliptical orbit with left focus at a given point
def generateEllipsePoints(centerX, centerY, semiMajorAxis, eccentricity, numPoints=1000):
    theta = np.linspace(0, 2 * np.pi, numPoints)
    c = semiMajorAxis * eccentricity
    a = semiMajorAxis
    b = a * np.sqrt(1 - eccentricity**2)
    x = centerX + c + a * np.cos(theta)
    y = centerY + b * np.sin(theta)
    return x, y

# Create the plot
fig, ax = plt.subplots()

# Plot the center point
sun = ax.scatter(0, 0, s=200, color='orange', marker='o', label='Sun')

# Plot the elliptical orbits with center at the sun
orbits = []
for planet in data:
    semiMajorAxis = planet[2]
    eccentricity = planet[6]

    x, y = generateEllipsePoints(0, 0, semiMajorAxis, eccentricity)
    orbit, = ax.plot(x, y, label=planet[0], alpha=0.1)
    orbits.append(orbit)

# Create lines for planet trails
planetTrails = [ax.plot([], [], '-', linewidth=1, alpha=0.5)[0] for _ in data]

# Create spherical objects for each planet
planetObjs = [ax.plot([], [], 'o', markersize=10)[0] for _ in data]


ax.scatter(0, 0, s=100, color='blue', marker='o', label='Earth')
# Set aspect ratio to 'equal' to ensure the plot shows circles as circles (ellipses as ellipses)
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
# Add labels and title
plt.xlabel('X (AU)')
plt.ylabel('Y (AU)')
plt.title('Nested Elliptical Orbits with Line Trails')

# Individual time factors for each orbit's motion
orbitSpeed = [20.11, 60.97, 157.5, 37.8]

# Number of frames for the planet trails
trail_length = 1000
trail_x = np.zeros((len(data), trail_length))
trail_y = np.zeros((len(data), trail_length))

# Function to update the animation
def update(frame):
    # Calculate the position of the center (Sun) on its orbit around the center
    sunX = np.cos(2 * np.pi * frame / 100)  # Orbiting at 1 AU radius
    sunY = np.sin(2 * np.pi * frame / 100)  # Orbiting at 1 AU radius

    sun.set_offsets((sunX, sunY))

    for i, planet in enumerate(data):
        semiMajorAxis = planet[2]
        eccentricity = planet[6]

        # Generate points for the orbit around the center
        x, y = generateEllipsePoints(sunX, sunY, semiMajorAxis, eccentricity, numPoints=10000)  # Generate more points

        # Calculate the position of the planet on the orbit using the time factor
        planetX = x[int(frame * orbitSpeed[i]) % len(x)]
        planetY = y[int(frame * orbitSpeed[i]) % len(y)]

        planetObjs[i].set_xdata(planetX)
        planetObjs[i].set_ydata(planetY)

        # Update planet trails
        trail_x[i, frame % trail_length] = planetX
        trail_y[i, frame % trail_length] = planetY

        # Interpolate to create smoother trails
        interp_indices = np.linspace(0, trail_length - 1, 1000)  # Increase the number of interpolated points
        interp_x = interp1d(np.arange(trail_length), trail_x[i], kind='cubic')(interp_indices)
        interp_y = interp1d(np.arange(trail_length), trail_y[i], kind='cubic')(interp_indices)

        planetTrails[i].set_data(interp_x, interp_y)

    return planetObjs + planetTrails + [sun]

# Create the animation
ani = FuncAnimation(fig, update, frames=range(1000), interval=(1000/300), blit=True)

# Show the plot
plt.grid(True)
plt.legend()
plt.show()







