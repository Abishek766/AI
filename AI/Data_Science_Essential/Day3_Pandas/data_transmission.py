import pandas as pd

Df = pd.DataFrame({'Information' : [1,2,3,4]})

# Df=Df.rename(columns={'Information':'interger'})
# print(Df)

# Df['interger']=Df['interger'].astype(float)
# print(Df.dtypes)
# print(Df)

# df=pd.DataFrame({'Date':['2023-01-01','2023-01-02','2023-01-03']})
# print("Before convertion: \n",df.dtypes)
# print(df)

# df['Date']=pd.to_datetime(df['Date'])
# print("After convertion: \n",df.dtypes)
# print(df)

Df['Multiple']=Df['Information']*2
print(Df)