import pandas as pd
import numpy as num

df1=pd.DataFrame(
    {"ID":[1,2,3],
     "Name":["Alice","Bob","Charlie"],
     "Age":[25,28,23]
    }
)
df2=pd.DataFrame({
    "ID":[1,2,3],
    "Score":[80,90,95]
})

print("Dataset 1 \n",df1)
print("Dataset 2 \n",df2)

merged=pd.merge(df1,df2, how="inner", on="ID")
print(merged)

merged["Score_Percentage"]=(merged["Score"]/100)*100
print("Data Transformation : \n", merged)