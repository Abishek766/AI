#url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

#Data Cleaning
df['total_bill']=df["total_bill"].fillna(0)
df['tip']=df['tip'].fillna(0)

#Define X and Y
X = df[['total_bill']]
Y= df['tip']

print("X: \n",X.head())
print("Y:  \n",Y.head())

#Training and testing Dataset
X_train,X_test,y_train,y_test=train_test_split(X, Y, test_size=0.2, random_state=42)
print("Traning Data Set: ",X_train.shape)
print("Testing Data Set: ",X_test.shape)

#Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Fitting the model
model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

plt.plot(y_test, color = 'blue', label='test')
plt.plot(y_pred,color='red',label='predictions')
plt.show()

#Model Evaluations
mse = mean_squared_error(y_test,y_pred)
print(mse)

mae = mean_absolute_error(y_test,y_pred)
print(mae)

r_square = r2_score(y_test,y_pred)
print(r_square)



