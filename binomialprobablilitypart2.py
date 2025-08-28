import matplotlib.pyplot as plt
from scipy.stats import binom
import numpy as np

# Parameters
n = 5         # number of coin tosses
p = 0.5       # probability of heads (success)
k = 3         # desired number of heads

# x-axis values (possible number of heads from 0 to 5)
x = np.arange(0, n + 1)
pmf = binom.pmf(x, n, p)
"""This calculates the probability of each number of successes in x for a binomial distribution with:

n = number of trials

p = probability of success in each trial

So this line gives you a list (array) of probabilities.

Example:
If n = 5, p = 0.5, and x = [0, 1, 2, 3, 4, 5],
then pmf will be:

python
Copy
Edit
[0.03125, 0.15625, 0.3125, 0.3125, 0.15625, 0.03125]

"""

# Print the probability of getting exactly 3 heads
prob_k = binom.pmf(k, n, p)
print(f"Probability of getting exactly {k} heads in {n} tosses: {prob_k:.4f}")

# Plot the PMF
plt.figure(figsize=(8, 5))
bars = plt.bar(x, pmf, color='lightblue', edgecolor='black')

# Highlight the bar for k = 3
bars[k].set_color('orange')
plt.axvline(k, color='red', linestyle='--', label=f'X = {k}')

# Labels and title
plt.title(f'Binomial PMF (n={n}, p={p})')
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
