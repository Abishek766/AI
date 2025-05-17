import pandas as pd

#Load DataSet
df=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

#Explore Structure
# print("First Five rows: \n",df.head())
# print("Last Five rows:\n",df.tail())

print(df.info())
print(df.describe())