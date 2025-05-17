import numpy as num

matrix= num.array([[1,2,3],[4,5,6],[7,8,9]])
print("Matrix : \n",matrix)

#Transpose
transpose=matrix.T
print("Transpose matrix: \n",transpose)

another_matrix=num.array([[9,8,7],[6,5,4],[3,2,1]])
print("Addition : \n",matrix+another_matrix)
print("Multiplication : \n",matrix*another_matrix)