import numpy as np
import matplotlib.pyplot as plt
vals=np.random.normal(0,0.5,10000)
plt.hist(vals,50)
plt.show()
print(np.mean(vals)) #1st moment
print(np.var(vals)) #2nd moment
import scipy.stats as sp
print(sp.skew(vals))
print(sp.kurtosis(vals))
