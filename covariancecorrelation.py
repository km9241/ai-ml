import matplotlib.pyplot as plt
import numpy as np
from pylab import *
def de_mean(x):
    xmean = mean(x)
    return [xi - xmean for xi in x]
'''his removes the mean from each value in the list x.
Example: If x = [2, 4, 6], then mean = 4 → de_mean(x) = [-2, 0, 2].
This step is part of the covariance formula:
Cov(X, Y) = [ Σ (Xi - X̄)(Yi - Ȳ) ] / (n - 1)
Σ = summation symbol (type: Alt + 228 on Windows or copy from here)
Xi, Yi = individual values of X and Y
X̄, Ȳ = mean of X and Y
n = number of data points
'''
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n-1)
'''his calculates covariance using:
dot(de_mean(x), de_mean(y)): This computes the sum of products of the de-meaned values.
n - 1: This makes it sample covariance (not population).'''
pageSpeeds = np.random.normal(3.0, 1.0, 1000)#pageSpeeds: Mean = 3.0 seconds, Std Dev = 1.0
purchaseAmount = np.random.normal(50.0, 10.0, 1000)#purchaseAmount: Mean = 50.0 dollars, Std Dev = 10.0
scatter(pageSpeeds, purchaseAmount)#This plots a scatter plot to visualize the relationship between pageSpeeds and purchaseAmount.
print(covariance (pageSpeeds, purchaseAmount))#This computes the covariance between the two datasets.
'''1. Based on Direction
Type	Description
🔼 Positive	As one variable increases, the other increases (e.g., height vs weight)
🔽 Negative	As one increases, the other decreases (e.g., speed vs time taken)
➖ Zero	No linear relationship between the variables'''
plt.show()
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds # As page speed decreases (faster page load), purchase amount increases.
scatter(pageSpeeds, purchaseAmount)
covariance (pageSpeeds, purchaseAmount)
plt.show()
#This function calculates the Pearson correlation coefficient (r) between two variables x and y.
def correlation(x, y):
    stddevx = x.std()#x.std() → standard deviation of x
    stddevy = y.std()#y.std() → standard deviation of y
    return covariance(x, y) / (stddevx * stddevy)
 # Always check for zero standard deviation to avoid division errors or misleading results.
#Cov(X,Y)/σXσY(formula)
print(correlation(pageSpeeds, purchaseAmount))
'''Negative sign → inverse relationship
Magnitude → moderately strong
'''
print(np.corrcoef(pageSpeeds, purchaseAmount))
'''1.0 on the diagonal means a variable is perfectly correlated with itself.
The off-diagonal values (like -0.68) show how strongly pageSpeeds and purchaseAmount are related.
when we say a variable is perfectly correlated with itself, it means the correlation coefficient is exactly 1.0.
That's why corrcoef(X, X) will always return 1.0
'''
#Strong negative relationship example        
purchaseAmount = 100 - pageSpeeds * 3
scatter(pageSpeeds, purchaseAmount)
print(correlation (pageSpeeds, purchaseAmount))
plt.show()
'''pageSpeeds is a set of random numbers centered around 3.
purchaseAmount = 100 - pageSpeeds * 3 creates a linear negative relationship.
 As pageSpeed increases (i.e., slower website), purchaseAmount decreases.
'''
#this out put is giving more than -1 need to find out reason????

'''Covariance just tells us the direction of the relationship:
Positive → both increase together
Negative → one increases, the other decreases
But it doesnot tell you how strong the relationship is unless you know the units.
Correlation takes covariance and scales it — so that it always lies between -1 and 1. This makes it much easier to interpret across different datasets.
'''





 

