import numpy as np

A=np.array([[2,3,4],[4,5,6],[7,8,9]])

#Determinant
determinant=np.linalg.det(A)
print("Determinant: ",determinant)

#Inverese of matrix Note: In square matrix does not have inverse of matrix. This will happen when det = 0

if determinant !=0:
    inverse=np.linalg.inv(A)
    print("Inverse of matrix: ",inverse)
else:
    print("Square matrix does not have inverse")

#eg2

B=np.array([[1,2,3],[6,5,7],[13,21,15]])

det1=np.linalg.det(B)
print("Determinant: ",det1)

inv1=np.linalg.inv(B)
print("Inverse: ",inv1)