import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

#Reading File
df = pd.read_csv(r"C:\Users\LENOVO\OneDrive\Desktop\AI\50_Startups.csv")

print(df.head(5))

#Data cleaning
print(df.info())

#Define inpendent and targer variables
X = df.iloc[:,:-1].values
Y = df.iloc[:,-1].values

print(X)
print(Y)

#Feature Encoding
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(),[3])], remainder='passthrough')
X=np.array(ct.fit_transform(X))
print(X)

#Train-Test-Size
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


#Create and fit the model
model = LinearRegression()
model.fit(X_train,y_train)
y_pred =model.predict(X_test)

#Plotting Y_test vs y_predict
plt.plot(y_test, color='blue', label='y_test')
plt.plot(y_pred,color='red',label='y-pred')
plt.show()

#Model Evalution
r2 = r2_score(y_test,y_pred)
print(r2)

#Test with out of box data
data = [[1.0,0.0,0.0,80000,125000,250000]]
new_df = pd.DataFrame(data)

new_df = sc.transform(new_df)

single=model.predict(new_df)
print(single)