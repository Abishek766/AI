import pandas as pd
import numpy as num

data ={
    "Name":["Alice","Bob",num.nan,"David"],
    "Age":[30,num.nan,28,35],
    "Score":[85,90,num.nan,88]
}
df=pd.DataFrame(data)
print("Orginal Dataset \n",df)

df["Name"]=df["Name"].fillna("NA")
df["Age"]=df["Age"].fillna(df["Age"].mean())
# df["Score"]=df["Score"].interpolate(method="polynomial", order=2)
df["Score"]=df["Score"].interpolate() #defalut method = linear

df=df.rename(columns={"Name":"Student_name","Score":"Exam_score"})
print("Dataset \n",df)
