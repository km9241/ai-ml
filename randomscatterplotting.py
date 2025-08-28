import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(500)  
y = np.random.randn(500)  
plt.scatter(x, y)
plt.title("Random Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()
'''randn stands for “random normal”, and it's used to generate random numbers from a standard normal distribution (also called a Gaussian distribution).
 In simple terms:
randn(n)
returns n random numbers from a bell-shaped curve centered at 0 with:
mean = 0
standard deviation = 1
 Example:
from numpy.random import randn
data = randn(5)
print(data)
Might output:
[ 0.54  -1.23  0.14  0.88  -0.77 ]
These numbers are more likely to be near 0, and less likely to be very far from 0.'''

