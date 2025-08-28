from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-3,3,0.001)
#plt.plot(x,norm.pdf(x))
#plt.savefig('C:\\pythonforml\\graphsaving\\testgraph1.png',format='png')#saves the graph in the location
#plt.show()
plt.plot(x,norm.pdf(x)) # Standard normal: mean=0, std=1
plt.plot(x,norm.pdf(x,1.0,0.5))# Custom normal: mean=1.0, std=0.5
'''Standard normal (again) — centered at 0, std = 1.

Custom normal:

Mean = 1.0 → the peak shifts right

Std = 0.5 → the curve becomes narrower and taller

'''
plt.savefig('C:\\pythonforml\\graphsaving\\testgraph1.png',format='png')#saves the graph in the location
plt.show()