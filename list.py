x=[1,2,3,4,5,6]
"""A list in Python is 
a built-in data type used to store a collection of items, such as numbers, strings, or even other lists."""
print(len(x)) #6
x[:3] #[1,2,3]
x[3:] #[4,5,6]
x[-2:] #[5,6]
x.extend([7,8])#[1,2,3,4,5,6,7,8]
x.append(9)#[1,2,3,4,5,6,7,8,9]
y=[10,11,12]
listoflist=[x,y]#in list you store anyything like 
z=[13,14,15]
z.sort()
z.sort(reverse=True)
print(z)



