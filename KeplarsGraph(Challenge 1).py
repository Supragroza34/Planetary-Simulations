import matplotlib.pyplot as ploty
import numpy as nump
import csv

def collector():
    global orbitalPeriod
    filePath = "data.txt"
    dataList = []
    orbitalPeriod = []
    with open(filePath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                dataValue = float(row[2])
                OrbitalValue = float(row[5])
                dataList.append(dataValue)
                orbitalPeriod.append(OrbitalValue)
                
    return dataList

semiAxis = collector()

Xpower = []
for x in semiAxis:
    Xpower.append(x**1.5)

#orbitalPeriod = [29.63, 84.75, 11.86, 0, 166.34, 248.35, 1.88, 0.62, 0.24, 1]
Planets = ["Saturn", "Uranus", "Jupiter", "Sun", "Neptune", "Pluto", "Mars", "Venus", "Mercury", "Earth"]
ploty.scatter(Xpower, orbitalPeriod, marker='x', color='b', label='Celestial Bodies')

ploty.xlabel('Distance from Sun^(3/2) / AU^(3/2)')
ploty.ylabel('Orbital Period / Years')
ploty.title("Kepler's 3rd Law")



for i in range(len(orbitalPeriod)):
    Spec = Planets[i]
    if Spec == "Mars" or Spec == "Venus" or Spec == "Mercury" or Spec == "Earth" or Spec == "Sun":
        ploty.text(Xpower[i], orbitalPeriod[i], "_", ha='right', va='bottom')
    else:
        ploty.text(Xpower[i], orbitalPeriod[i], Spec, ha='right', va='bottom')
    #ploty.text(Xpower[i], orbitalPeriod[i], f"Body {i+1}", ha='right', va='bottom')



#calculates coefficients that approximate the relationship between distance and orbital period.
coeff = nump.polyfit(Xpower, orbitalPeriod, 1)

#poly1d function allows you to create a polynomial object that can be formed for any value.
bestFitLine = nump.poly1d(coeff)
bestFitLine[0] = 0 #indicates the intercept of the line is at (0,0)


#Line of best is drawn
ploty.plot(Xpower, bestFitLine(Xpower), color='r', label='Line of Best fit')

ploty.grid(True)
ploty.legend()
ploty.show()
