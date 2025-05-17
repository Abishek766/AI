import pandas as pd

data = {
    "Department": ["HR", "IT", "HR", "IT", "Finance", "HR", "Finance"],
    "Employee": ["A", "B", "C", "D", "E", "F", "G"],
    "Salary": [50000, 60000, 55000, 70000, 65000, 52000, 67000],
}

df=pd.DataFrame(data)


def range_func(x):
    return x.max() - x.min()

group=df.groupby('Department')['Salary'].agg(range_func)
print(group)