from scipy.stats import poisson# suppose the average sale of an shop is 500 then what the probablity of sales goinng upto 550
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(400, 601)#x axis from 400 to 600
plt.plot(x, poisson.pmf(x, 500))
"""
 In a Poisson PMF plot, the y-axis represents:
The probability of getting exactly x events (like arrivals, defects, heads, etc.) when the average rate is μ.
"""
plt.show()
