import numpy as num

arr=num.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#in numpy library we want to specify the axies for row and columns 0 means column and 1 means row
row_sum=num.sum(arr, axis=1)
col_sum=num.sum(arr, axis=0)
print("Row addition: ",row_sum)
print("Column addition: ",col_sum)