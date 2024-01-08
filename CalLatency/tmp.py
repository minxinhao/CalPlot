import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y = 10 ** x

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y)

# Set the y-axis label
ax.set_ylabel('Values (10$^x$)')

# Show the plot
plt.show()