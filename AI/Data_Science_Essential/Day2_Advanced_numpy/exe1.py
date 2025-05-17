import numpy as num

matrix=num.array([[1,2,3],[4,5,6],[7,8,9]])
vector=num.array([1,0,-1])

result_add=matrix+vector
print("Addition: \n",result_add)

result_mul=matrix*vector
print("Multiplication: \n",result_mul)

result_rem=matrix % 2
print("Remainder: \n",result_rem)