import pandas as pd

data={
    "Class":['A','B','A','B','C','C'],
    "Score":[85,90,88,72,95,80],
    "Age":[15,16,15,17,16,15]
}

df=pd.DataFrame(data)

print("Original Dataset \n",df)

group=df.groupby("Class").mean()
print(group)