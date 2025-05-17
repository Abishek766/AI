import numpy as num

arr=num.array([1,2,3,4,5,6])

even=arr[arr % 2==0]
print("Even: ",even)

#Modified array based on conditions
arr[arr > 3]=0
print("Modified: ",arr)