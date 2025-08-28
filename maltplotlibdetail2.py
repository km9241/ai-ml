from scipy.stats import norm              
import matplotlib.pyplot as plt           
import numpy as np                       
#Create an array of x values from -5 to 5 with small intervals 0.001
x = np.arange(-5, 5, 0.001)
axes = plt.axes()
'''Think of it like:
plt.axes() = create the graph area (like a blank sheet for drawing).

axes = the name of that graph area.

Now you can say things like:

axes.set_xlim(...) → set the left/right limits.

axes.set_ylim(...) → set the up/down limits.

axes.grid() → show grid lines.

'''
# Set x-axis range from -5 to 5
axes.set_xlim([-5, 5])
# Set y-axis range from 0 to 1.0
axes.set_ylim([0, 1.0])
# Set specific tick marks on the x-axis
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
# Set specific tick marks on the y-axis
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
# Display grid lines on the plot
axes.grid()
# Set custom label for the x-axis
plt.xlabel('Greebles')
# Set custom label for the y-axis
plt.ylabel('Probability')
# Plot standard normal distribution (mean=0, std=1) in blue solid line
plt.plot(x, norm.pdf(x), 'b-')
# Plot custom normal distribution (mean=1.0, std=0.5) in red dotted line
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'r:')
# Add legend to the plot with labels for each curve; loc=4 puts it in the lower-right
plt.legend(['Sneetches', 'Gacks'], loc=4)
plt.show()
