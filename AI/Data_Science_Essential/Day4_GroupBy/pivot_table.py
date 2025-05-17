import pandas as pd
import numpy as num

# data={
#     'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
#     'Sub-Category': ['X', 'X', 'Y', 'Y', 'X', 'Y'],
#     'Sales': [100, 200, 150, 250, 120, 300]
# }

# df=pd.DataFrame(data)
# pivot=df.pivot_table(
#     values='Sales',
#     index='Category',
#     columns='Sub-Category',
#     aggfunc='sum'
# )
# print(pivot)

# Pivot_table using Multiple Aggregation
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'C', 'C'],
    'Sub-Category': ['X', 'X', 'Y', 'Y', 'X', 'Y', 'X', 'Y'],
    'Sales': [100, 200, 150, 250, 120, 300, 180, 160],
    'Profit': [30, 40, 35, 50, 25, 60, 45, 55]
}

df=pd.DataFrame(data)
pivot=df.pivot_table(
    values=['Sales','Profit'],
    index='Category',
    columns='Sub-Category',
    aggfunc={'Sales':'sum','Profit':'mean'},
    fill_value=0
)
print(pivot)

#Pivot_Table using multiple index
# df=pd.DataFrame(data)
# pivot_df=df.pivot_table(
#     values='Sales',
#     index=['Category','Sub-Category'],
#     aggfunc='sum'
# )
# print(pivot_df)
