import numpy as np

#2 x 2 matrix
A=np.array([[1,2],[3,4]])

U, S, vt=np.linalg.svd(A)
print("Singular values: ",S)
print("Left singular vector: \n",U)
print("Vector Transpose: \n",vt)

# To show a result in matrix 
#Reconstruct

Sigma=np.zeros((2,2))
np.fill_diagonal(Sigma, S)
recontruct=U @ Sigma @vt #Apply formula
print("Reconstructed matrix: \n",recontruct)

# 3 x 3 matrix
B=np.array([[1,2,1],[3,4,5],[8,9,10]])

U1, S1, vt1=np.linalg.svd(B)
print("Singular values: ",S1)
print("Left singular vector: \n",U1)
print("Vector Transpose: \n",vt1)

# To show a result in matrix 
#Reconstruct

Sigma1=np.zeros((3,3))
np.fill_diagonal(Sigma1, S1)
recontruct1=U1 @ Sigma1 @vt1 #Apply formula
print("Reconstructed matrix: \n",recontruct1)