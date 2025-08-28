"""Generate random numbers:

np.random.rand(): Random floats in the range [0.0, 1.0).

np.random.randn(): Random samples from a normal distribution (mean = 0, std = 1).

np.random.randint(): Random integers within a specified range.

Random sampling:

np.random.choice(): Randomly pick items from an array.

np.random.shuffle(): Shuffle elements in an array in-place.

np.random.permutation(): Return a shuffled copy of an array.

Distributions:

np.random.normal(loc, scale, size): Draw samples from a normal (Gaussian) distribution.

np.random.uniform(low, high, size): Uniform distribution.

np.random.binomial(n, p, size): Binomial distribution.

Many more (Poisson, exponential, etc.)"""
import numpy as np

# Random float between 0 and 1
print(np.random.rand())

# Random integer between 1 and 10
print(np.random.randint(1, 11))

# Random choice from a list
print(np.random.choice([10, 20, 30, 40]))

arr = np.array([1, 2, 3, 4])
np.random.shuffle(arr)  # Shuffles in place

# mean = 100 (loc), std dev = 10 (scale)
numbers = np.random.normal(loc=100, scale=10, size=5)
print(numbers)
"""loc=100 = Numbers will be around 100

scale=10 = They will vary +or-10 or so

size=5 = You get 5 numbers"""
