import numpy as np

#Create Identtity Matrix
I=np.eye(3)
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("\n",np.dot(I,A))

#Zero Matrix
print("Zero Matrix: \n",np.zeros((3,3)))

#Diagonal Matrix
print("Diagonal Matrix: \n",np.diag([4,5,6]))

