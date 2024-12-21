import numpy as nump
import matplotlib.pyplot as ploty


auToM = 1.496e11

# The data for the planets is presented in the format planet, mass (Earth masses), distance (AU), radius (Earth radii), rotational period (days), orbital period (years)
planetData = [
    ["Saturn", 95.16, 9.58, 9.45, 0.44, 29.63],
    ["Uranus", 14.50, 19.29, 4.01, 0.72, 84.75],
    ["Jupiter", 317.85, 5.20, 11.21, 0.41, 11.86],
    ["Sun", 332837, 0, 109.12, 0, 0],
    ["Neptune", 17.20, 30.25, 3.88, 0.67, 166.34],
    ["Mars", 0.107, 1.523, 0.53, 1.03, 1.88],
    ["Venus", 0.815, 0.723, 0.95, 243.02, 0.62],
    ["Mercury", 0.055, 0.387, 0.38, 58.65, 0.24],
    ["Earth", 1, 1, 1, 1, 1]
]


fig, ax = ploty.subplots(figsize=(8, 8))

# Plot the orbits
for planetInfo in planetData:
    planet, mass, distance, radius, _, orbitalPeriod = planetInfo
    if planet == "Sun":
        continue  # Skip the Sun as it is already placed at (0,0)

    distanceToM = distance * auToM

    theta = nump.linspace(0, 2 * nump.pi, 100) # creates an array of evenly spaced values within a specified range. the format is .linspace(start, stop, number of evenly spaced values)
    xCoords = distanceToM * nump.cos(theta)
    yCoords = distanceToM * nump.sin(theta)

    # Plot the orbit
    ax.plot(xCoords / auToM, yCoords / auToM, label=planet)

# Set labels and title
ax.set_xlabel("X (AU)")
ax.set_ylabel("Y (AU)")
ax.set_title("Elliptical Orbits of Planets")

# Set aspect ratio to equal to show orbits as circles
ax.set_aspect('equal')

# Set axis limits
ax.set_xlim(-31, 31)
ax.set_ylim(-31, 31)

# Add legend
ax.legend() #essentially a visual guide that shows and explains all meanings of different elements

# Show the plot
ploty.show()






#Code below


















"""#OUTER PLANETS ONLY
import matplotlib.pyplot as ploty
import numpy as nump

# Given data (planet_name, mass_earth, distance_au, rotational_period_days, orbital_period_years, eccentricity)
data = [
    ["Saturn", 95.16, 9.58, 9.45, 0.44, 29.63, 0.06],
    ["Uranus", 14.50, 19.29, 4.01, 0.72, 84.75, 0.05],
    ["Jupiter", 317.85, 5.20, 11.21, 0.41, 11.86, 0.05],
    ["Neptune", 17.20, 30.25, 3.88, 0.67, 166.34, 0.01],
]
#semi major axis  = SMA
# Function to generate points for the elliptical orbit with at the sun
def generate_ellipse_points(SMA, ecc, num_points=1000):
    #Shorthanded see smaller planets to understand what happens here
    theta = nump.linspace(0, 2 * nump.pi, num_points)
    c = SMA * ecc
    a = SMA
    b = a * nump.sqrt(1 - ecc**2)
    x = c + a * nump.cos(theta)
    y = b * nump.sin(theta)
    return x, y

# Create the plot
fig, ax = ploty.subplots()

# Plot the sun at (0, 0)
ax.scatter(0, 0, s=200, color='yellow', marker='o', label='Sun')

# Plot the elliptical orbits
for planet in data:
    SMA = planet[2]
    ecc = planet[6]

    x, y = generate_ellipse_points(SMA, ecc)
    ax.plot(x, y, label=planet[0])

# Set aspect ratio to equal
ax.set_aspect('equal')

# Add labels and title
ploty.xlabel('X (AU)')
ploty.ylabel('Y (AU)')
ploty.title('Elliptical Orbits of Planets of the sun')

# Show the plot
ploty.grid(True)
ploty.legend()
ploty.show()

# Whilst it looks like there is no eccentricity applied, look at the orbits of uranus and Neptune, it is evident that they are not symmetrical along x = 0"""















#Code below










#Inner planets

"""import matplotlib.pyplot as ploty
import numpy as nump

# Given data (planetName, massEarth, distanceAU, rotationalPeriodDays, orbitalPeriodYears, eccentricity)
data = [
    ["Mars", 0.107, 1.523, 0.53, 1.03, 1.88, 0.09],
    ["Venus", 0.815, 0.723, 0.95, 243.02, 0.62, 0.01],
    ["Mercury", 0.055, 0.387, 0.38, 58.65, 0.24, 0.21],
    ["Earth", 1, 1, 1, 1, 1, 0.02],
]

# Function to generate points for the elliptical orbit of the sun
def generateEllipsePoints(semiMajorAxis, eccentricity, numPoints=1000):

    # Generate an array of angles theta ranging from 0 to 2pi.
    theta = nump.linspace(0, 2 * nump.pi, numPoints)

    # Calculate the distance from the origin to the center of the ellipse along the major axis.
    c = semiMajorAxis * eccentricity

    # Assign the semi-major axis to variable 'a'.
    a = semiMajorAxis

    # Calculate the semi-minor axis of the ellipse using the eccentricity and semi major axis value
    b = a * nump.sqrt(1 - eccentricity**2)

    # Calculate the X coordinates
    xCoords = c + a * nump.cos(theta) # c value obviously determines the shift / change in orbit pattern due to eccentricity

    # Calculate the Y coordinates
    yCoords = b * nump.sin(theta)

    # Return the x and y coordinates of the generated points on the ellipse for further calculations
    return xCoords, yCoords

# Create the plot
fig, ax = ploty.subplots()

# Plot the sun at (0, 0)
ax.scatter(0, 0, s=200, color='yellow', marker='o', label='Sun')

# Plot the elliptical orbits of the sun
for planet in data:
    semiMajorAxis = planet[2]
    eccentricity = planet[6]

    xCoords, yCoords = generateEllipsePoints(semiMajorAxis, eccentricity)
    ax.plot(xCoords, yCoords, label=planet[0])

# Set aspect ratio to 'equal' to ensure the plot shows circles as circles (ellipses as ellipses)
ax.set_aspect('equal')

# Add labels and title
ploty.xlabel('X (AU)')
ploty.ylabel('Y (AU)')
ploty.title('Elliptical Orbits of Planets of the Sun')

# Show the plot
ploty.grid(True)
ploty.legend()
ploty.show()"""


