import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.metrics import r2_score
from sklearn.pipeline import Pipeline

X= 6 * np.random.rand(200,1)-3
Y=0.8 * X**2 + 0.9 * X + 2 + np.random.randn(200, 1)

# print(X)

plt.plot(X,Y,'b.')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

#Train test split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#Applying linear regression model
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

r2 = r2_score(y_test, y_pred)
print(r2)

#Applying polynomial Regression

ply = PolynomialFeatures(degree=2, include_bias=True)
X_train_trans= ply.fit_transform(X_train)
X_test_trans = ply.transform(X_test)

#Fit the model
lr2 = LinearRegression()
lr2.fit(X_train_trans, y_train)
y_pred = lr2.predict(X_test_trans)

#model evalution
r2 = r2_score(y_test, y_pred)
print(r2)

# when degree = 2 r2 = 0.88

#Testing with new data
x_new = np.linspace(-3,3,200).reshape(200,1)
x_new_poly = ply.transform(x_new)
y_new = lr2.predict(x_new_poly)

plt.plot(x_new,y_new,"r.", linewidth=2, label='Prediction')
plt.plot(X_train,y_train,"b.", label = 'Traning')
plt.plot(X_test, y_test, 'g.', label='Test')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

