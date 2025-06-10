import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import r2_score

#Load Dataset
housing = fetch_california_housing()
data = pd.DataFrame(housing.data, columns=housing.feature_names)
target = pd.DataFrame(housing.target , columns=['Price'])
df = pd.concat([data, target], axis=1)

# print(df.head(5))

#  MedInc  HouseAge  AveRooms  AveBedrms  Population  AveOccup  Latitude  Longitude  Price
# 0  8.3252      41.0  6.984127   1.023810       322.0  2.555556     37.88    -122.23  4.526
# 1  8.3014      21.0  6.238137   0.971880      2401.0  2.109842     37.86    -122.22  3.585
# 2  7.2574      52.0  8.288136   1.073446       496.0  2.802260     37.85    -122.24  3.521
# 3  5.6431      52.0  5.817352   1.073059       558.0  2.547945     37.85    -122.25  3.413
# 4  3.8462      52.0  6.281853   1.081081       565.0  2.181467     37.85    -122.25  3.422
# df.to_csv('fetch_california_housing')

#Spliting data into features and target
X=df.drop('Price' , axis=1)
Y=df['Price']

#split the data into train test split
X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.2, random_state=0)

# print(len(df)) 20640
# print(len(X_train)) 16512
# print(len(X_test)) 4128

#Apply linear regression model
model1 = LinearRegression()
model1.fit(X_train,y_train)
y_pred1 = model1.predict(X_test)

#Model Evalution
r2=r2_score(y_test,y_pred1)
# print(r2) 
# r2 score for model1 = 0.5943232652466202

#Apply ridge regression
model2 = Ridge(alpha=0.5)
model2.fit(X_train, y_train)
y_pred2=model2.predict(X_test)

r2_1=r2_score(y_test,y_pred2)
# print(r2_1)
# r2 score for model2 = 0.5943153839288556
#Apply lesso regression
model3 = Lasso(alpha=0.5)
model3.fit(X_train, y_train)
y_pred3=model3.predict(X_test)

r2_2=r2_score(y_test,y_pred2)
# print(r2_2) 0.5943153839288556

#Optimizing the features using lesso
#Goal remove unwanted features or irrelavent features
bad_features = np.where(model3.coef_==0)[0]
print('Features with bad_feature: ',list(X.columns[bad_features]))

#Remove these features
X_train_filtered = X_train.drop(X_train.columns[bad_features], axis=1)
X_test_filtered = X_test.drop(X_test.columns[bad_features], axis=1)

# Applying lasso regression,and linear regression on filter data
model_lr = LinearRegression()
model_lr.fit(X_train_filtered, y_train)
y_pred_filter_lr = model_lr.predict(X_test_filtered)
print("R2 score for filtered data: ", r2_score(y_test,y_pred_filter_lr))

model_lesso = Lasso(alpha=0.1)
model_lesso.fit(X_train_filtered,y_train)
y_pred_filter_lesso = model_lesso.predict(X_test_filtered)
print("R2 score for filtered data: ", r2_score(y_test,y_pred_filter_lesso))