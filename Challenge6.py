import numpy as nump
import matplotlib.pyplot as ploty
from matplotlib.animation import FuncAnimation

planetData = [
    ["Mars", 0.107, 1.523, 0.53, 1.03, 1.88, 0.09],
    ["Venus", 0.815, 0.723, 0.95, 243.02, 0.62, 0.01],
    ["Mercury", 0.055, 0.387, 0.38, 58.65, 0.24, 0.21],
    ["Earth", 1, 1, 1, 1, 1, 0.02],
]

massVenusEarthMasses = 0.815
distanceVenusAu = 0.723
eccentricityVenus = 0.01
orbitalPeriodVenusYears = 0.62

massEarthEarthMasses = 1
distanceEarthAu = 1
eccentricityEarth = 0.02
orbitalPeriodEarthYears = 1

distanceVenusM = distanceVenusAu * 1.496e11
distanceEarthM = distanceEarthAu * 1.496e11
massVenusKg = massVenusEarthMasses * 5.972e24
massEarthKg = massEarthEarthMasses * 5.972e24
orbitalPeriodVenusS = orbitalPeriodVenusYears * 365.25 * 86400
orbitalPeriodEarthS = orbitalPeriodEarthYears * 365.25 * 86400

def generateEllipsePoints(semiMajorAxis, eccentricity, numPoints=1000):
    theta = nump.linspace(0, 2 * nump.pi, numPoints)
    c = semiMajorAxis * eccentricity
    a = semiMajorAxis
    b = a * nump.sqrt(1 - eccentricity**2)
    xCoords = c + a * nump.cos(theta)
    yCoords = b * nump.sin(theta)
    return xCoords, yCoords

fig, ax = ploty.subplots()

def planetPosition(time, distanceM, massKg, orbitalPeriodS, eccentricity, inclinationRad=0):
    meanAnomaly = (2 * nump.pi * time) / orbitalPeriodS
    trueAnomaly = meanAnomaly
    distanceSun = distanceM
    x = distanceSun * nump.cos(trueAnomaly)
    y = distanceSun * nump.sin(trueAnomaly) * nump.cos(inclinationRad)
    return x, y

orbits = []
for planet in planetData:
    semiMajorAxis = planet[2]
    ecc = planet[5]
    x, y = generateEllipsePoints(semiMajorAxis, ecc)
    orbit, = ax.plot(x, y, label=planet[0])
    orbits.append(orbit)

ax.set_xlim(-2e11, 2e11)
ax.set_ylim(-2e11, 2e11)

venus, = ax.plot([], [], 'o', markersize=5, color='orange', label='Venus')
earth, = ax.plot([], [], 'o', markersize=5, color='blue', label='Earth')
connectionLine, = ax.plot([], [], '-', color='purple', alpha=0.8)
sun, = ax.plot([0], [0], 'o', markersize=10, color='yellow', label='Sun')

lines = []
venusPathX = []
venusPathY = []
earthPathX = []
earthPathY = []

intervalSum = 10 / 1234
print(intervalSum)

def update(frame):
    # Calculate time in seconds for Earth and Venus
    timeEarth = frame * 86400
    timeVenus = frame * 86400 * (2/1.446)  # Constant needed to multiply Venus's speed

    # Calculate positions of Venus and Earth based on time and orbital parameters
    xVenus, yVenus = planetPosition(timeVenus, distanceVenusM, massVenusKg, orbitalPeriodVenusS, eccentricityVenus)
    xEarth, yEarth = planetPosition(timeEarth, distanceEarthM, massEarthKg, orbitalPeriodEarthS, eccentricityEarth)

    # Update positions of Venus and Earth in the plot
    venus.set_data(xVenus, yVenus)
    earth.set_data(xEarth, yEarth)

    # Update the connection line between Venus and Earth
    connectionLine.set_data([xVenus, xEarth], [yVenus, yEarth])

    # Append positions to path lists for plotting paths
    venusPathX.append(xVenus)
    venusPathY.append(yVenus)
    earthPathX.append(xEarth)
    earthPathY.append(yEarth)

    # Draw a line and store it in the 'lines' list every 0.015 seconds
    if frame % 5 == 0:
        line, = ax.plot([xVenus, xEarth], [yVenus, yEarth], '-', color='red', alpha=0.1, linewidth=0.9)
        lines.append(line)
        ploty.pause(0.015)

    # Plot the orbits as continuous lines
    numPointsOrbit = 1000
    venusOrbitX, venusOrbitY = generateEllipsePoints(distanceVenusM, eccentricityVenus, numPointsOrbit)
    earthOrbitX, earthOrbitY = generateEllipsePoints(distanceEarthM, eccentricityEarth, numPointsOrbit)
    venusOrbit, = ax.plot(venusOrbitX, venusOrbitY, '-', color='orange', alpha=0.3)
    earthOrbit, = ax.plot(earthOrbitX, earthOrbitY, '-', color='blue', alpha=0.3)

    # Return the updated plot elements for animation
    return venus, earth, connectionLine, sun, venusOrbit, earthOrbit

ax.set_aspect("equal")
numFrames = 1500
ploty.xlabel('X (AU)')
ploty.ylabel('Y (AU)')
ani = FuncAnimation(fig, update, frames=numFrames, interval=0.2, blit=True)
ax.legend()
ploty.show()
