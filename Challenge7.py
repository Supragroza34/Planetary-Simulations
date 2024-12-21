import matplotlib.pyplot as plt
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
sun = ax.scatter(0, 0, s=200, color='orange', marker='o', label='Sun')

# Create spherical objects for each planet
planetObjs = [ax.plot([], [], 'o', markersize=10, label=planet[0])[0] for planet in data]

# Create line objects for planet trails with different colors
trailColors = ['blue', 'green', 'red', 'purple']  # Colors for planet trails
planetTrails = [ax.plot([], [], color=color, alpha=0.3)[0] for color in trailColors]

# Set aspect ratio to 'equal' to ensure the plot shows circles as circles (ellipses as ellipses)
ax.set_aspect('equal')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Add labels and title
plt.xlabel('X (AU)')
plt.ylabel('Y (AU)')
plt.title("Ptolemy's Model of the Universe")
earth = ax.scatter(0, 0, s=200, color='blue', marker='o', label='Earth')

# Individual time factors for each orbit's motion
planetOrbitSpeed = [16.01, 5.598, 40, 2.852]  # Planet orbit speeds reduced by a factor of 10 to be able to
sunOrbitSpeed = 2.6  # Sun's orbit speed (adjust as needed)

# Adjustable center distance
sunDistance = 1.5  # Adjust the distance as needed

# Lists to store previous positions for each planet
prevPlanetPositions = [[] for _ in data]

# Function to update the animation
def update(frame):
    # Calculate the position of the (Sun) on its orbit around the center
    sunX = sunDistance * np.cos(2 * np.pi * frame * sunOrbitSpeed / 1000)  # Adjusted sun's orbit speed
    sunY = sunDistance * np.sin(2 * np.pi * frame * sunOrbitSpeed / 1000)  # Adjusted sun's orbit speed

    sun.set_offsets((sunX, sunY))

    for i, planet in enumerate(data):
        semiMajorAxis = planet[2]
        eccentricity = planet[6]

        # Generate points for the orbit around the center
        x, y = generateEllipsePoints(sunX, sunY, semiMajorAxis, eccentricity)

        # Calculate the position of the planet on the orbit using the time factor
        planetX = x[int(frame * planetOrbitSpeed[i]) % len(x)]
        planetY = y[int(frame * planetOrbitSpeed[i]) % len(y)]

        planetObjs[i].set_xdata(planetX)
        planetObjs[i].set_ydata(planetY)

        # Update the previous positions list
        prevPlanetPositions[i].append((planetX, planetY))

        # Limit the length of the previous positions list to create the fading trail effect
        maxTrailLength = 20000
        if len(prevPlanetPositions[i]) > maxTrailLength:
            prevPlanetPositions[i] = prevPlanetPositions[i][-maxTrailLength:]

        # Update planet trails
        trailX, trailY = zip(*prevPlanetPositions[i])
        planetTrails[i].set_xdata(trailX)
        planetTrails[i].set_ydata(trailY)

    return planetObjs + [sun] + planetTrails

# Create the animation
ani = FuncAnimation(fig, update, frames=range(10000), interval=(1000/3000), blit=True)

# Show the plot
plt.grid(True)
plt.legend()
plt.show()
