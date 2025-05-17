import numpy as np

#Element wise operation(Addition and Substraction)

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])

# print("Addition: \n",a+b)
# print("Substraction: \n",a-b)

# #Scalar Multiplication

# C= 2*a
# print("Scalar Multiplication: \n",C)

#Matrix Multiplication
result= np.dot(a,b)
# print("Matrix Multiplication \n",result)

#Identity matrix
I=np.eye(3)
# print("Identity matrix: \n",I)

#Zero Matrix
Z=np.zeros((2,3))
print("Zero Matrix: \n",Z)