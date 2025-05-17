import pandas as pd

s=pd.Series([10,20,30],index=("A","B","C"))
print(s)

data={"Name":["Alice","Bob"],"Age":[10,20]}
dataset=pd.DataFrame(data)
print(dataset)