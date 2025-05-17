import numpy as np

#Determinant
A=np.array([[2,3],[1,4]])
Determinant=np.linalg.det(A)
#print("Determinant: ",Determinant)

#Inverse matrix
inverse=np.linalg.inv(A)
#print("Inverse Matrix \n",inverse)

#Eigenvaluse and EigenVectors

eigenvalues, eigenvectors=np.linalg.eig(A)
# print("Eigen Values: \n",eigenvalues)
# print("Eigen Vectors: \n",eigenvectors)

#SVD (Singular Vector Dimensions)
U, S, Vt=np.linalg.svd(A)
print("U: ",U)
print("Singluar Matrix: \n",S)
print("Vector Transpose: \n",Vt)