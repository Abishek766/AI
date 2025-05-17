import pandas as pd

#Concatenation 
df1=pd.DataFrame({'A':[1,2],'B':[3,4]})
df2=pd.DataFrame({'A':[5,6],'B':[7,8]})

combined_rows=pd.concat([df1,df2], axis=0) # affecting columns A,B
print(combined_rows)
combined_colums=pd.concat([df1,df2],axis=1) # affecting rows index 0 ,1 
print(combined_colums)

# Merging

df1=pd.DataFrame({'ID':[1,2,3],'Name':['Alice','Bob','Charlie']})
df2=pd.DataFrame({'ID':[2,3,4],'scorce':[90,85,95]})

#inner merging
result=pd.merge(df1,df2, on='ID', how='inner')
print(result)

#outer merging
result=pd.merge(df1,df2, on='ID', how='outer')
print(result)

#left merging
result=pd.merge(df1,df2, on='ID', how='left')
print(result)

#right merging
result=pd.merge(df1,df2, on='ID', how='right')
print(result)

#Merging two different columns
df3=pd.DataFrame({'USERID':[2,3,4],'scorce':[100,20,10]})

result=pd.merge(df1,df3, left_on='ID',right_on='USERID',how='inner')
print(result)

#Joins 

df1=pd.DataFrame({'Name':['Alice','bob','charlie']},index=[1,2,3])
df2=pd.DataFrame({'Score':[95,80]},index=[2,3])

result=df1.join(df2)
print(result)

#inner
result=df1.join(df2, how='inner')
print(result)

#outer
result=df1.join(df2, how='outer')
print(result)

#right
result=df1.join(df2, how='right')
print(result)

#Joining with column_names

df1=pd.DataFrame({'ID':[1,2,3],'Name':['Alice','bob','charlie']})
df2=pd.DataFrame({'User_Id':[2,3],'score':[90,95]})

result=df1.set_index('ID').join(df2.set_index('User_Id'), how='inner')
print(result)

# Handling duplicate columns

df1=pd.DataFrame({'ID':[1,2,3],'Value':[90,100,20]})
df2=pd.DataFrame({'User_Id':[1,2,3],'Value':[10,50,500]})

result=df1.set_index('ID').join(df2.set_index('User_Id'), lsuffix='_df1', rsuffix='_df2', how='outer')
print(result)
