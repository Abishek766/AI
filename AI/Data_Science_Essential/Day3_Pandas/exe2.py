import pandas as pd

#Load DataSet
df=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

#print(df.info())

selected_column=df[["species","sepal_length"]]
print("Selected Columns \n",selected_column)

fliter_rows=df[(df["sepal_length"]> 5.0)&(df["species"] =="setosa")]
print("Filter Rows: \n",fliter_rows)