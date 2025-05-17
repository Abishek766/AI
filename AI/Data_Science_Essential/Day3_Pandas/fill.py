import pandas as pd

data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Temperature': [30, 32, None, 35, None, None, 40, 42, None, 45]
})
# Displaying the dataset
print("Original Data:")
print(data)

#forward fill
data['Temperature_ffill'] = data['Temperature'].ffill()

# print("Data with Forward Fill:")
# print(data[['Date', 'Temperature', 'Temperature_ffill']])

#Backward fill
data['Temperature_bfill'] = data['Temperature'].bfill()

# print("Data with Backward Fill:")
# print(data[['Date', 'Temperature', 'Temperature_bfill']])

print(data[['Date', 'Temperature', 'Temperature_ffill','Temperature_bfill']])

