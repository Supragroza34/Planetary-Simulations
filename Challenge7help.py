import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Given data (planetName, massEarth, distanceAU, radiusEarthRadii, rotationalPeriodDays, orbitalPeriodYears, eccentricity)
data = [
    ["Mars", 0.107, 1.523, 0.53, 1.03, 1.88, 0.09],
    ["Venus", 0.815, 0.723, 0.95, 243.02, 0.62, 0.01],
    ["Mercury", 0.055, 0.387, 0.38, 58.65, 0.24, 0.21],
]

def generateEllipsePoints(centerX, centerY, semiMajorAxis, eccentricity, numPoints=1000):
    theta = np.linspace(0, 2 * np.pi, numPoints)
    c = semiMajorAxis * eccentricity
    a = semiMajorAxis
    b = a * np.sqrt(1 - eccentricity**2)
    x = centerX + c + a * np.cos(theta)
    y = centerY + b * np.sin(theta)
    return x, y

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

sun = ax.scatter([0], [0], [0], s=200, color='orange', marker='o', label='Sun')
planetObjs = [ax.plot([], [], [], 'o', markersize=10, label=planet[0])[0] for planet in data]

trail_colors = ['blue', 'green', 'red', 'purple']
planetTrails = [ax.plot([], [], [], color=color, alpha=0.3)[0] for color in trail_colors]

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)

ax.set_xlabel('X (AU)')
ax.set_ylabel('Y (AU)')
ax.set_zlabel('Z (AU)')
ax.set_title("Ptolemy's Model of the Universe")

planetOrbitSpeed = [2.011, 6.097, 15.75, 3.78]
sunOrbitSpeed = 2.6

sunDistance = 1.5
prevPlanetPositions = [[] for _ in data]

def update(frame):
    sunX = sunDistance * np.cos(2 * np.pi * frame * sunOrbitSpeed / 1000)
    sunY = sunDistance * np.sin(2 * np.pi * frame * sunOrbitSpeed / 1000)

    sun._offsets3d = ([sunX], [sunY], [0])

    for i, planet in enumerate(data):
        semiMajorAxis = planet[2]
        eccentricity = planet[6]

        x, y = generateEllipsePoints(sunX, sunY, semiMajorAxis, eccentricity)

        planetX = x[int(frame * planetOrbitSpeed[i]) % len(x)]
        planetY = y[int(frame * planetOrbitSpeed[i]) % len(y)]

        planetObjs[i].set_xdata([planetX])
        planetObjs[i].set_ydata([planetY])
        planetObjs[i].set_3d_properties([0])

        prevPlanetPositions[i].append((planetX, planetY, 0))

        max_trail_length = 20000
        if len(prevPlanetPositions[i]) > max_trail_length:
            prevPlanetPositions[i] = prevPlanetPositions[i][-max_trail_length:]

    for i in range(len(planetTrails)):
        planetTrails[i]._verts3d = zip(*prevPlanetPositions[i])

    return planetObjs + [sun] + planetTrails

ani = FuncAnimation(fig, update, frames=range(10000), interval=(1000/3000), blit=True)

plt.grid(True)
plt.legend()
plt.show()
