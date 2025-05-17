import numpy as np

#Create Matrix
A=np.array([[1,2],[3,4]])
B=np.array([[9,8],[7,6]])

#Addition
print("Addition: \n",A+B)

#Substraction
print("Substraction: \n",A-B)

#Multiplication
print("Multiplication: \n",np.dot(A,B))

#Scalar Multiplication
print("Scalar Multiplication: \n",2*A)