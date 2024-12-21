


"""import matplotlib.pyplot as plt
import numpy as np

# amplitude and phase definition
ampList = [1,2,4]
phaseList = [0,10,20]

# center coordinates of the first circle
C_x = 0
C_y = 0

# generate figure and axis
fig, ax = plt.subplots()

# loop over each amplitude and phase
for amp, phase in zip(ampList, phaseList):

    # draw current circle
    circle = plt.Circle((C_x, C_y), amp, fill = False)
    ax.add_patch(circle)
    # draw current circle center
    ax.plot(C_x, C_y, marker = 'o', markerfacecolor = 'k', markeredgecolor = 'k')

    # compute next circle center
    C_x += amp*np.cos(np.deg2rad(phase))
    C_y += amp*np.sin(np.deg2rad(phase))

# adjust axis
plt.axis("equal")
plt.xlim( -10 , 10 )
plt.ylim( -10 , 10 )

# show the plot
plt.show()"""







import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

freqList = [1, 2, 3]
ampList = [1, 2, 4]
phaseList = [0, 10, 20]

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize the center coordinates of the gray dot
dot, = ax.plot(0, 0, marker='o', color='gray', label='Orbiting Dot')

# Set axis limits
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Create a list to store the circles
circles = []

# Create a list to store the paths of the gray dot
dot_paths = []

# Function to update the plot at each frame of the animation
def update(frame):
    global dot
    x = 0
    y = 0

    for i in range(len(freqList)):
        theta = np.linspace(0, 2 * np.pi, 150)
        x += ampList[i] * np.cos(theta * freqList[i] + phaseList[i])
        y += ampList[i] * np.sin(theta * freqList[i] + phaseList[i])

    dot.set_data(x[frame], y[frame])

    # Draw the circles
    for i in range(len(freqList)):
        circle = plt.Circle((0, 0), ampList[i], fill=False)
        circles.append(circle)
        ax.add_patch(circle)

        dot_path, = ax.plot(x[:frame + 1], y[:frame + 1], color='gray', linewidth=1, alpha=0.5)
        dot_paths.append(dot_path)

    return circles + [dot] + dot_paths

# Total number of frames
numFrames = 150

# Create the animation
ani = FuncAnimation(fig, update, frames=numFrames, interval=100, blit=True)

# Add a legend to the plot
ax.legend()

# Show the plot
plt.show()
