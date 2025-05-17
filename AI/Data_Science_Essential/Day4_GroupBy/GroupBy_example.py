import pandas as pd

data = {
    "Department": ["HR", "IT", "HR", "IT", "Finance", "HR", "Finance"],
    "Employee": ["A", "B", "C", "D", "E", "F", "G"],
    "Salary": [50000, 60000, 55000, 70000, 65000, 52000, 67000],
}

df=pd.DataFrame(data)

#grouped=df.groupby("Department")
#print(grouped) # note we cannot do groupby alone, we need aggregate function

#Operation
#iteration

# for name, group in grouped:
#     print(f"Department,{name}")
#     print(group)

#Aggregation Functions
#group=df.groupby("Department")["Salary"].sum() one way
#print(group)

#another wa
# sum_salary=grouped["Salary"].sum() y
# print(sum_salary)

#Multiple aggregation
group=df.groupby("Department")["Salary"].agg(["sum","mean","max"])
print(group)