from scipy.stats import binom  #What's the probability of getting 3 heads in 5 coin tosses, if the coin is fair (i.e., success probability = 0.5)
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(6)
pmf = binom.pmf(x, 5, 0.5)

plt.bar(x, pmf)
plt.title("Binomial PMF (n=5, p=0.5)")
plt.show()
