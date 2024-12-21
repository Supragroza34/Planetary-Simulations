import numpy as nump
import matplotlib.pyplot as ploty
from scipy.interpolate import interp1d

# Define function to calculate orbit angle vs. time
def angleVsTime(t, P, ecc, theta_V):
    dTheta = 1 / 1000  # Angle step for simpsons rule

    # Number of orbits
    N = nump.ceil(t[-1] / P)  # Calculate the number of complete orbits based on the given time array

    # Define an array of polar angles for orbits
    theta = nump.arange(theta_V, 2 * nump.pi * N + theta_V + dTheta, dTheta)  # Generate an array of polar angles covering multiple orbits

    # Evaluate the integrand of the time integral
    f = (1 - ecc * nump.cos(theta))**(-2)  # Compute the function to be integrated over polar angles

    #%Define Simpson rule coefficients c = [ 1, 4, 2, 4, 2, 4, ....
    L = len(theta)
    isOdd = nump.where(nump.arange(1, L - 1) % 2 == 1, 4, 2)
    coeffs = nump.concatenate(([1], isOdd, [1]))

    # Calculate an array of times using Simpson's rule
    tt = (P * (1 - ecc**2)**(3/2) * (1 / (2 * nump.pi)) * dTheta * (1/3)
          * nump.cumsum(coeffs * f))

    # Create the interpolation function for polar angles
    thetaInterp = interp1d(tt, theta, kind='cubic', fill_value="extrapolate")
    # Interpolate polar angles

    # Calculate polar angles at the given time points
    thetaCalculated = thetaInterp(t)  # Interpolate polar angles for the specified time points

    return thetaCalculated  # Return the calculated polar angles corresponding to the given time array


# Orbital parameters for Pluto
semiMajorPluto = 39.51
eccPluto = 0.25
periodPluto = 248.35


# Time values
timeValuesPluto = nump.linspace(0, 3 * periodPluto, num=1000)

# Calculate orbit angle theta for the circular orbit
thetaCircular = 2 * nump.pi * (timeValuesPluto / periodPluto)

# Calculate orbit angle theta using the numerical method for the eccentric orbit
thetaCalculated = angleVsTime(timeValuesPluto, periodPluto, eccPluto, 0)

# Plot the orbit angle vs. time
ploty.plot(timeValuesPluto, thetaCalculated, label='Eccentric Orbit (ε = 0.25)')
ploty.plot(timeValuesPluto, thetaCircular, 'r-', label='Circular Orbit')
ploty.xlabel('Time (years)')
ploty.ylabel('Orbit Angle (radians)')
ploty.title('Orbit Angle vs. Time for Eccentric and Circular Orbits')
ploty.legend()
ploty.grid(True)
ploty.show()
