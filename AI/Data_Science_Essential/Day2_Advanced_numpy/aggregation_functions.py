import numpy as num

arr=num.array([[1,2,3],[4,5,6]])

print("Sum: ",num.sum(arr))
print("Mean: ",num.mean(arr))
print("Maximum value: ",num.max(arr))
print("Minimum value: ",num.min(arr))
print("Standard Deviation: ",num.std(arr))
print("Sum along the rows: ",num.sum(arr, axis=1))
print("Sum along the columns: ",num.sum(arr, axis=0))