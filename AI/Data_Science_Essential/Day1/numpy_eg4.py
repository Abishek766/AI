import numpy as num

arr=num.array([10,20,30,40,50,60])
#Indexing
print(arr[2])
print(arr[-1])

#Slicing
print(arr[1:4])
print(arr[:3])
print(arr[4:])

#Reshape
reshaped=arr.reshape(2,3)
print(reshaped)