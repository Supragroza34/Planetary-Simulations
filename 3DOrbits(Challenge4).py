
#Big Planets
import matplotlib.pyplot as ploty
import numpy as nump
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Given data (planetName, massEarth, distanceAU, rotationalPeriodDays, orbitalPeriodYears, eccentricity, inclinationDegrees)
planetData = [
    ["Saturn", 95.16, 9.58, 9.45, 0.44, 29.63, 0.06, 2.49],
    ["Uranus", 14.50, 19.29, 4.01, 0.72, 84.75, 0.05, 0.77],
    ["Jupiter", 317.85, 5.20, 11.21, 0.41, 11.86, 0.05, 1.31],
    ["Neptune", 17.20, 30.25, 3.88, 0.67, 166.34, 0.01, 1.77],
    ["Pluto", 0.003, 39.51, 0.19, 6.39, 248.35, 0.25, 17.5]
]

# Function to generate points for the elliptical orbit of the sun
def generateEllipsePoints(semiMajorAxis, eccentricity, inclination, numPoints=1000):
    theta = nump.linspace(0, 2 * nump.pi, numPoints)
    c = semiMajorAxis * eccentricity
    a = semiMajorAxis
    b = a * nump.sqrt(1 - eccentricity ** 2)
    xCoords = c + a * nump.cos(theta)
    yCoords = b * nump.sin(theta)

    # Apply inclination to the orbit
    inclinationRad = nump.deg2rad(inclination)
    xRot = xCoords
    yRot = yCoords * nump.cos(inclinationRad)
    zRot = yCoords * nump.sin(inclinationRad)

    return xRot, yRot, zRot

# Create the plot
fig = ploty.figure()
ax = fig.add_subplot(111, projection='3d')

# Swap and reverse the x and y axes
ax.set_xlim(40, -20)  # Reverse the X-axis direction
ax.set_ylim(-max([planet[2] for planet in planetData]) * 1.5, max([planet[2] for planet in planetData]) * 1.5)  # Reverse the Y-axis direction
ax.set_zlim(-20, 20)  # Extend the Z-axis to 20

# Plot the sun at (0, 0, 0)
ax.scatter(0, 0, 0, s=200, color='yellow', marker='o', label='Sun')

# Plot the elliptical orbits of the sun
orbits = []
for planetInfo in planetData:
    semiMajorAxis = planetInfo[2]
    eccentricity = planetInfo[6]
    inclination = planetInfo[7] + 180  # Adjust the inclination angle by 180 degrees

    xCoords, yCoords, zCoords = generateEllipsePoints(semiMajorAxis, eccentricity, inclination)

    # Create the orbits (3D lines)
    orbit, = ax.plot(xCoords, yCoords, zCoords, label=planetInfo[0])
    orbits.append(orbit)

# Create spherical objects for each planet
planetObjects = [ax.plot([], [], [], 'o', markersize=10)[0] for _ in planetData]

# Set aspect ratio to 'equal' to ensure the plot shows circles as circles (ellipses as ellipses)
ax.set_aspect('equal')

# Add labels and title
ax.set_xlabel('Y (AU)')  # Swap x and y axis labels
ax.set_ylabel('X (AU)')  # Swap x and y axis labels
ax.set_zlabel('Z (AU)')
ax.set_title('Elliptical Orbits of Planets of the Sun')

# Change the camera angle (elevation and azimuthal angles)
ax.view_init(elev=10, azim=310)  # Adjust the angles as desired

# Individual time factors for each planet's orbital motion (adjust these values to control the speed of each orbit)
# Calculated by finding the frames per second and then accordingly
orbitSpeedFactors = [16.01, 5.598, 40, 2.852, 1.91]  # Added value for Pluto

# Function to update the animation
def update(frame):
    for i, planetInfo in enumerate(planetData):
        semiMajorAxis = planetInfo[2]
        eccentricity = planetInfo[6]
        inclination = planetInfo[7]

        # Generate points for the orbit
        xCoords, yCoords, zCoords = generateEllipsePoints(semiMajorAxis, eccentricity, inclination)

        # Calculate the position of the planet on the orbit using the time factor
        planetX = xCoords[int(frame * orbitSpeedFactors[i]) % len(xCoords)]
        planetY = yCoords[int(frame * orbitSpeedFactors[i]) % len(yCoords)]
        planetZ = zCoords[int(frame * orbitSpeedFactors[i]) % len(zCoords)]

        # Convert inclination angle to radians for rotation
        inclinationRad = nump.deg2rad(inclination)

        # Apply rotation to adjust planet position in 3D space
        planetXRot = planetX * nump.cos(inclinationRad) - planetY * nump.sin(inclinationRad)
        planetYRot = planetX * nump.sin(inclinationRad) + planetY * nump.cos(inclinationRad)

        # Set the updated X, Y, and Z coordinates for the planet's marker
        planetObjects[i].set_data(planetXRot, planetYRot)
        planetObjects[i].set_3d_properties(planetZ)

    # Return the updated planet markers to indicate changes in the plot
    return planetObjects

# Create the animation
# Increase the number of frames to be a multiple of the longest orbit's frames (Saturn's orbit has 1000 frames)
animation = FuncAnimation(fig, update, frames=range(5000), interval=25, blit=True)

# Show the plot
ploty.grid(True)
ploty.legend()
ploty.show()









"""#Small Planets

import matplotlib.pyplot as plt
import numpy as nump
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Given data (planetName, massEarth, distanceAU, rotationalPeriodDays, orbitalPeriodYears, eccentricity, inclinationDegrees)
data = [
    ["Mars", 0.107, 1.523, 0.53, 1.03, 1.88, 0.09, 1.85],
    ["Venus", 0.815, 0.723, 0.95, 243.02, 0.62, 0.01, 3.39],
    ["Mercury", 0.055, 0.387, 0.38, 58.65, 0.24, 0.21, 7],
    ["Earth", 1, 1, 1, 1, 1, 0.02, 0]
]

# Function to generate points for the elliptical orbit of the sun
def generateEllipsePoints(semiMajorAxis, eccentricity, inclination, numPoints=1000):
    theta = nump.linspace(0, 2 * nump.pi, numPoints)
    c = semiMajorAxis * eccentricity
    a = semiMajorAxis
    b = a * nump.sqrt(1 - eccentricity ** 2)
    x = c + a * nump.cos(theta)
    y = b * nump.sin(theta)

    # Apply inclination to the orbit
    inclinationRad = nump.deg2rad(inclination)
    xRot = x
    yRot = y * nump.cos(inclinationRad)
    zRot = y * nump.sin(inclinationRad)

    return xRot, yRot, zRot

# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.set_xlim(4, -4)
ax.set_ylim(4, -4)
ax.set_zlim(-2, 2)

# Plot the sun at the  (0, 0, 0)
ax.scatter(0, 0, 0, s=200, color='yellow', marker='o', label='Sun')

# Plot the elliptical orbits of the sun
orbits = []
for planet in data:
    semiMajorAxis = planet[2]
    eccentricity = planet[6]
    inclination = planet[7]

    x, y, z = generateEllipsePoints(semiMajorAxis, eccentricity, inclination)

    # Create the orbits (3D lines)
    orbit, = ax.plot(x, y, z, label=planet[0])
    orbits.append(orbit)

# Create spherical objects for each planet
planetObjs = [ax.plot([], [], [], 'o', markersize=10)[0] for _ in data]

# Set aspect ratio to 'equal' to ensure the plot shows circles as circles (ellipses as ellipses)
ax.set_aspect('equal')

# Add labels and title
ax.set_xlabel('Y (AU)')  
ax.set_ylabel('X (AU)')  
ax.set_zlabel('Z (AU)')
ax.set_title('Elliptical Orbits of Planets of the Sun')

# Change the camera angle (elevation and azimuthal angles)
ax.view_init(elev=20, azim=130)  # Adjust the angles as desired

# Individual time factors for each planet's orbital motion (adjust these values to control the speed of each orbit)
# Calculated by finding the frames per second and then accordingly
orbitSpeedFactors = [20.11, 60.97, 157.5, 37.8]  # Added value for Pluto

# Function to update the animation
def update(frame):
    for i, planet in enumerate(data):
        semiMajorAxis = planet[2]
        eccentricity = planet[6]
        inclination = planet[7]

        # Generate points for the orbit (fixed, not spinning)
        x, y, z = generateEllipsePoints(semiMajorAxis, eccentricity, inclination)

        # Calculate the position of the planet on the orbit using the time factor
        planetX = x[int(frame * orbitSpeedFactors[i]) % len(x)]
        planetY = y[int(frame * orbitSpeedFactors[i]) % len(y)]
        planetZ = z[int(frame * orbitSpeedFactors[i]) % len(z)]

        inclinationRad = nump.deg2rad(inclination)
        planetXRot = planetX * nump.cos(inclinationRad) - planetY * nump.sin(inclinationRad)
        planetYRot = planetX * nump.sin(inclinationRad) + planetY * nump.cos(inclinationRad)
        # For other planets, keep the x-coordinates as they are (no rotation in XY plane)
        planetXRot = planetX
        planetYRot = planetY

        planetObjs[i].set_data(planetXRot, planetYRot)
        planetObjs[i].set_3d_properties(planetZ)

    return planetObjs

# Create the animation
ani = FuncAnimation(fig, update, frames=range(315), interval=33.333, blit=True)

# Show the plot
plt.grid(True)
plt.legend()
plt.show()"""

































