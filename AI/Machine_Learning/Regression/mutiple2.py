from sklearn.datasets import make_regression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as ps
import plotly.graph_objects as gs

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import plotly.io as pio

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Plotly does not show interactive plots in the VS Code terminal by default
# Unlike matplotlib, which can open a static window, plotly relies on an interactive renderer (like a browser or notebook cell).
# Set Plotly to open plots in browser
pio.renderers.default = 'browser'

#Creating Synthetic Data
X, y = make_regression(n_samples=100, n_features=2, n_informative=2, n_targets=1, noise=50)
df = pd.DataFrame({'feature1':X[:,0], 'feature2':X[:,1], 'target':y})
# print(df.head(5))

#genertating 3d Plot
fig = ps.scatter_3d(df, x='feature1', y='feature2', z='target')
# fig.show()

#Train and Teat
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3)

#Creating and fit the model
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

#Model Evaluation
mae = mean_absolute_error(y_test, y_pred)
print(mae)

mse = mean_squared_error(y_test, y_pred)
print(mse)

r2 = r2_score(y_test,y_pred)
print(r2)