import numpy as np
import matplotlib.pyplot as plt

vals = np.random.normal(0, 0.5, 10000)  # Generate 10,000 random values from a normal distribution (mean=0, std=0.5)
plt.hist(vals, 50)                     # Plot a histogram with 50 bins
plt.show()                             # Display the plot

print(np.percentile(vals, 50))         # Print the 50th percentile (median)
print(np.percentile(vals, 20))         # Print the 20th percentile
