import pandas as pd
import numpy as num

df=pd.read_csv(r"C:\Users\LENOVO\Downloads\vgsales.csv")
#sprint(df)



# # for name, group in grouped:
# #     print("Publisher: ",name)
# #     print(group)

#pivot table

# pivot=df.pivot_table(
#     values=['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales'],
#     index='Publisher',
#     columns=['Name','Platform','Year','Genre'],
#     aggfunc={'NA_Sales':'sum','EU_Sales':'max','JP_Sales':'mean','Other_Sales':'min','Global_Sales':'sum'},
#     fill_value=0
# )

# print(pivot)

#custom varience

def varience(x):
    return num.var(x)

def sum_func(y):
    return y.sum()
def max_func(z):
    return z.max()
def renge_func(k):
    return k.max()-k.min()
def standard_deviation(m):
    return m.std()

grouped=df.groupby("Publisher").agg(
    {'NA_Sales':varience,'EU_Sales':sum_func,'JP_Sales':max_func,'Other_Sales':renge_func,'Global_Sales':standard_deviation}
    )
print(grouped)