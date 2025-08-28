import numpy as np
import matplotlib.pyplot as plt
income=np.random.normal(27000,19000,10000)
print(np.mean(income))
plt.hist(income,50)
plt.show()
print(income.std())#standard deviation
print(income.var())#variance

#import matplotlib_inline #use jypter notebook
#import matplotlib.pyplot as plt
plt.hist(income,50)#This line creates a histogram of the income data using 50 bins.x = values y = frecuency
plt.show()
print(np.median(income))
income=np.append(income,10000000000)#salary of ellon musk suppose
#mediam does not change but mean does
ages = np.random.randint(18,high=90,size=500)
'''18: the lowest value that can be included (inclusive).

high=90: the highest value not included (exclusive).

size=500: generate 500 random numbers in this range.

'''
print(ages)
from scipy import stats #to mind mode has other function too
print(stats.mode(ages))

values = np.random.uniform(-10, 10, 100000)#Every number in the range you specify (in your case, from -10 to 10) has an equal chance of being selected.
"""f you used np.random.normal(0, 1, 100000), that would give you a bell curve (normal distribution) where values around 0 are more common, and values far from 0 are rare.
"""







