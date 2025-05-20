import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#Generate Data
np.random.seed(42)
x=np.random.rand(100,1) * 10
y=np.random.randn(100,1) * 2

#Fit the data
model = LinearRegression()
model.fit(x,y)

#Get Coefficient
slope = model.coef_[0][0]
intercept = model.intercept_[0]
score = model.score(x,y)

#Visualize
plt.scatter(x,y, color="blue", label="Data")
plt.plot(x, model.predict(x), color="red", label="Linear Regression")
plt.legend()
plt.show()