import numpy as np
import matplotlib.pyplot as plt

# Generate data
uniform_values = np.random.uniform(-10, 10, 100000)
normal_values = np.random.normal(0, 5, 100000)  # mean = 0, std dev = 5



# Uniform Distribution
plt.subplot(1, 2, 1)
plt.hist(uniform_values, bins=50, color='skyblue', edgecolor='black')
plt.title('Uniform Distribution (-10 to 10)')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Normal Distribution
plt.subplot(1, 2, 2)
plt.hist(normal_values, bins=50, color='salmon', edgecolor='black')
plt.title('Normal Distribution (mean=0, std=5)')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
