import numpy as np

x = np.ones((3,3))
y = np.zeros((3,3))
print(np.add(x,y))
print(np.ndim(x))
print(np.shape(x))
print(np.size(x))
print(type(x))

w= np.array([[11,12],[13,14], [15,16]])

z= np.array([1,2])

newArray= np.vstack((w,z))

for i in newArray:
     print(i)

print(newArray.transpose())
newArray += 1
print(newArray)
print(newArray.min())
print(newArray.max())
print(newArray[0:1])
print(newArray[newArray==12])
print(newArray[0,1])
print(newArray)
#print(newArray.reshape(9,1))
#print(newArray.reshape(3,2))
#we can not change the shape because size = 8







