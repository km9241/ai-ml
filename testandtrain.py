import numpy as np
from pylab import *
import matplotlib.pyplot as plt
np.random.seed(2)#So the result is the same every time
pagespeed=np.random.normal(3.0,1.0,100)#100 values with mean 3.0,standarddev 1.0
purchaseamount=np.random.normal(50.0,30.0,100)/pagespeed #slower pages → fewer purchases
scatter(pagespeed,purchaseamount)
plt.show()
trainX = pagespeed[:80]
testX = pagespeed[80:]
trainY = purchaseamount[:80]
testY = purchaseamount[80:]
#Helps avoid overfitting (model performing well on training but poorly on new data).
scatter(trainX,trainY)
plt.show()
scatter(testX,testY)
plt.show()
#plotting for training data
x=np.array(trainX)
y=np.array(trainY)
p4=np.poly1d(np.polyfit(x,y,8))
#np.polyfit(x, y, 8) fits a polynomial of degree 8 to the training data.
#np.poly1d(...) creates a polynomial function p4 which you can use like p4(x).
'''If xp = [0, 0.1, ..., 7]
and p4(xp) = [120, 110, ..., 30]
then plt.plot(xp, p4(xp), c='r') draws a red curve through those points.
'''
xp=linspace(0,7,100)# 100 points between 0 and 7
axes=plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0,200])
plt.scatter(testX,testY)
plt.plot(xp,p4(xp),c='r')
#This line draws a smooth red curve using your polynomial model. Let's break it down:
#Y-axis values — these are the predicted purchase amounts for each value in xp using your polynomial model p4.
plt.show()
#plotting for test data
testx = np.array(testX)
testy = np.array(testY)
axes = plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0, 200])
plt.scatter(testx, testy)
plt.plot(xp, p4(xp), c='r')  
plt.show()
from sklearn.metrics import r2_score
r2=r2_score(trainY,p4(trainX)) #R² (R-squared): Measures model accuracy (1 = perfect fit, 0 = no fit).
print(r2)
r2_test = r2_score(testY, p4(testX))
print("Test R² score:", r2_test)
r2_train = r2_score(trainY, p4(trainX))
print("Training R² score:", r2_train)
'''Training R²: Tells you how well the model fits the training data.
Test R²: Tells you how well the model generalizes to new, unseen data.
If training R² >> test R², you're probably overfitting (especially with degree 8)'''









