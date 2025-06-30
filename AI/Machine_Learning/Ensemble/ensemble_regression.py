import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import BaggingRegressor, RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_regression
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.model_selection import train_test_split

#Create dataset
X, y = make_regression(n_samples=10000, n_features=10, n_informative=3 , random_state=42)

X_train, X_test, y_train , y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Feature Scaling
sc = StandardScaler()
X_train_sc = sc.fit_transform(X_train)
X_test_sc = sc.transform(X_test)

#Decision Tree
model_dt = DecisionTreeRegressor()
model_dt.fit(X_train_sc,y_train)
y_pred_dt = model_dt.predict(X_test_sc)

print("Decision Tree r2-score: ",r2_score(y_test,y_pred_dt))
print("Decision Tree mae: ",mean_absolute_error(y_test,y_pred_dt))
print("Decision Tree mse: ",mean_squared_error(y_test,y_pred_dt))
print("Decision Tree rmse: ",np.sqrt(mean_squared_error(y_test,y_pred_dt)))

#Bagging (Decision Tree)
bag_dt = BaggingRegressor(estimator=DecisionTreeRegressor(), 
                           n_estimators=500, 
                           max_samples=0.50, 
                           bootstrap= True, random_state=42)


bag_dt.fit(X_train_sc,y_train)
y_pred_bagdt = bag_dt.predict(X_test_sc)

print("BR r2-score: ",r2_score(y_test,y_pred_bagdt))
print("BR mae: ",mean_absolute_error(y_test,y_pred_bagdt))
print("BR mse: ",mean_squared_error(y_test,y_pred_bagdt))
print("BR rmse: ",np.sqrt(mean_squared_error(y_test,y_pred_bagdt)))
#Random Forest
rf = RandomForestRegressor(n_estimators=500, random_state=42)
rf.fit(X_train_sc,y_train)
y_pred_rf = rf.predict(X_test_sc)

print("RF r2-score: ",r2_score(y_test,y_pred_rf))
print("RF mae: ",mean_absolute_error(y_test,y_pred_rf))
print("RF mse: ",mean_squared_error(y_test,y_pred_rf))
print("RF rmse: ",np.sqrt(mean_squared_error(y_test,y_pred_rf)))
#Bagging (SVM)
bag_svm = BaggingRegressor(estimator=SVR(), 
                           n_estimators=500, 
                           max_samples=0.25, 
                           bootstrap= True, random_state=42)
bag_svm.fit(X_train_sc,y_train)
y_pred_svr = bag_svm.predict(X_test_sc)

print("BR(SVR) r2-score: ",r2_score(y_test,y_pred_svr))
print("BR(SVR) mae: ",mean_absolute_error(y_test,y_pred_svr))
print("BR(SVR) mse: ",mean_squared_error(y_test,y_pred_svr))
print("BR(SVR) rmse: ",np.sqrt(mean_squared_error(y_test,y_pred_svr)))
#Pasting
pasting = BaggingRegressor(estimator=DecisionTreeRegressor(), 
                           n_estimators=500, 
                           max_samples=0.50, 
                           bootstrap= False, random_state=42)
pasting.fit(X_train_sc,y_train)
y_pred_pas = pasting.predict(X_test_sc)

print("Pasting r2-score: ",r2_score(y_test,y_pred_pas))
print("Pasting mae: ",mean_absolute_error(y_test,y_pred_pas))
print("Pasting mse: ",mean_squared_error(y_test,y_pred_pas))
print("Pasting rmse: ",np.sqrt(mean_squared_error(y_test,y_pred_pas)))

# Model	              R2_Score	MAE	  MSE	RMSE
# DecisionTreeRegressor	0.97	7.9	 126.3	11.24
# BaggedRegressor	        0.99	3.4	 40.5	6.36
# RandomForest Regressor	0.99	3.2	 34.43	5.8
# BaggedRegressor(SVR)	0.74	25.74 1519	38
# Pasting	                0.99	3.4	 38.54	6.2

#Random Forest is best fitting model for this datasets