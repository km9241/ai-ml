import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the normal distribution
mean = 170
std_dev = 10

# Generate a range of height values
x = np.arange(140, 200, 0.5)  # smaller step for smooth curve

# Calculate the PDF values using scipy.stats.norm.pdf
pdf = norm.pdf(x, loc=mean, scale=std_dev)

# Plot the PDF
plt.plot(x, pdf, label='Mean = 170, SD = 10')
plt.title('Height Distribution of Kids')
plt.xlabel('Height (cm)')
plt.ylabel('Probability Density')
plt.show()
