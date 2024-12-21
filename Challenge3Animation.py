
#Outer Planets
"""import matplotlib.pyplot as ploty
import numpy as nump
from matplotlib.animation import FuncAnimation

# Given data (planetName, massEarth, distanceAU, rotationalPeriodDays, orbitalPeriodYears, eccentricity)
data = [
    ["Saturn", 95.16, 9.58, 9.45, 0.44, 29.63, 0.06],
    ["Uranus", 14.50, 19.29, 4.01, 0.72, 84.75, 0.05],
    ["Jupiter", 317.85, 5.20, 11.21, 0.41, 11.86, 0.05],
    ["Neptune", 17.20, 30.25, 3.88, 0.67, 166.34, 0.01],
]

# Function to generate points for the elliptical orbit of the sun
def generateEllipsePoints(semiMajorAxis, eccentricity, numPoints=1000):
    theta = nump.linspace(0, 2 * nump.pi, numPoints)
    c = semiMajorAxis * eccentricity
    a = semiMajorAxis
    b = a * nump.sqrt(1 - eccentricity**2)
    x = c + a * nump.cos(theta)
    y = b * nump.sin(theta)
    return x, y

# Create the plot
fig, ax = ploty.subplots()

sun = ax.scatter(0, 0, s=200, color='yellow', marker='o', label='Sun')

orbits = []
for planet in data:
    semiMajorAxis = planet[2]
    eccentricity = planet[6]

    x, y = generateEllipsePoints(semiMajorAxis, eccentricity)
    orbit, = ax.plot(x, y, label=planet[0])
    orbits.append(orbit)

# Create spherical objects for each planet
planetObjects = [ax.plot([], [], 'o', markersize=10)[0] for _ in data]

# Set aspect ratio to 'equal' to ensure the plot shows circles as circles and eccentricity will be noticeable
ax.set_aspect('equal')

# Add labels and title
ploty.xlabel('X (AU)')
ploty.ylabel('Y (AU)')
ploty.title('Elliptical Orbits of Planets of the Sun')

# Individual time factors for each planet's orbital motion (adjust these values to control the speed of each orbit)
# Calculated by finding the frames per second and then accordingly
orbitSpeedFactors = [16.01, 5.598, 40, 2.852]

# Function to update the animation
def update(frame):
    for i, planet in enumerate(data):
        semiMajorAxis = planet[2]
        eccentricity = planet[6]

        # Generate points for the orbit (fixed, not spinning)
        x, y = generateEllipsePoints(semiMajorAxis, eccentricity)

        # Calculate the position of the planet on the orbit using the time factor
        planetX = x[int(frame * orbitSpeedFactors[i]) % len(x)]
        planetY = y[int(frame * orbitSpeedFactors[i]) % len(y)]
        planetObjects[i].set_xdata(planetX)
        planetObjects[i].set_ydata(planetY)

    return planetObjects

# Create the animation
ani = FuncAnimation(fig, update, frames=range(1000), interval=(1000/30), blit=True)

# Show the plot
ploty.grid(True)
ploty.legend()
ploty.show()"""














#Inner planets
import matplotlib.pyplot as ploty
import numpy as nump
from matplotlib.animation import FuncAnimation

# Given data (planetName, massEarth, distanceAU, radiusEarthRadii, rotationalPeriodDays, orbitalPeriodYears, eccentricity)
planetData = [
    ["Mars", 0.107, 1.523, 0.53, 1.03, 1.88, 0.09],
    ["Venus", 0.815, 0.723, 0.95, 243.02, 0.62, 0.01],
    ["Mercury", 0.055, 0.387, 0.38, 58.65, 0.24, 0.21],
    ["Earth", 1, 1, 1, 1, 1, 0.02],
]

# Function to generate points for the elliptical orbit of the sun
def generateEllipsePoints(semiMajorAxis, eccentricity, numPoints=1000):
    theta = nump.linspace(0, 2 * nump.pi, numPoints)
    c = semiMajorAxis * eccentricity
    a = semiMajorAxis
    b = a * nump.sqrt(1 - eccentricity**2)
    xCoords = c + a * nump.cos(theta)
    yCoords = b * nump.sin(theta)
    return xCoords, yCoords

# Create the plot
fig, ax = ploty.subplots()

sunMarker = ax.scatter(0, 0, s=200, color='yellow', marker='o', label='Sun')

orbitLines = []
for planetInfo in planetData:
    semiMajorAxis = planetInfo[2]
    eccentricity = planetInfo[6]

    xCoords, yCoords = generateEllipsePoints(semiMajorAxis, eccentricity)
    orbitLine, = ax.plot(xCoords, yCoords, label=planetInfo[0])
    orbitLines.append(orbitLine)

# Create spherical objects for each planet
planetMarkers = [ax.plot([], [], 'o', markersize=10)[0] for _ in planetData]

# Set aspect ratio to 'equal' to ensure the plot shows circles as circles and eccentricity will be noticeable
ax.set_aspect('equal')

# Add labels and title
ploty.xlabel('X (AU)')
ploty.ylabel('Y (AU)')
ploty.title('Elliptical Orbits of Planets of the Sun')

# Individual time factors for each planet's orbital motion, dependent on number of frames and interval
orbitSpeed = [20.11, 60.97, 157.5, 37.8]

# Function to update the animation
def update(frame):
    for i, planetInfo in enumerate(planetData):
        semiMajorAxis = planetInfo[2]
        eccentricity = planetInfo[6]

        # Generate points for the orbit
        xCoords, yCoords = generateEllipsePoints(semiMajorAxis, eccentricity)

        # Calculate the position of the planet on the orbit using the time factor
        planetX = xCoords[int(frame * orbitSpeed[i]) % len(xCoords)]
        planetY = yCoords[int(frame * orbitSpeed[i]) % len(yCoords)]

        # Set the calculated coordinates as the new data for the planet's marker
        planetMarkers[i].set_xdata(planetX)
        planetMarkers[i].set_ydata(planetY)

    return planetMarkers

# Create the animation
animation = FuncAnimation(fig, update, frames=range(315), interval=(1000/30), blit=True)

# Show the plot
ploty.grid(True)
ploty.legend()
ploty.show()













