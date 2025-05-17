import numpy as np

A=np.array([[15,14],[20,25]])

eigenvalues, eigenvectors=np.linalg.eig(A)
print("Eigenvalues are: ",eigenvalues)
print("Eigenvectors are: \n",eigenvectors)