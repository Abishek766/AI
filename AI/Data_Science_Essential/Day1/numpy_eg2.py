import numpy as num

arr=num.array(["Abi","Dhivay","Durga","Aravindth","Pradap","ECE"])
reshaped=arr.reshape((2,3))
print(reshaped);

#add dimensions

arr=num.array([1,2,3,4,5])
expand=arr[:, num.newaxis]
print(expand)