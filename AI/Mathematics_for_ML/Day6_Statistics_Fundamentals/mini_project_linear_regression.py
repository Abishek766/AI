#Implement the mathematical formula for linear regression

import numpy as np

np.random.seed(42)
X = 2*np.random.randn(100,1)
y = 4 + 3 * X + np.random.randn(100,1)

#Add bias term to features matrix
X_b = np.c_[np.ones((100,1)),X]

#Initial parameters
theta = np.random.randn(2,1)
learning_rate = 0.1
iterations = 1000

def predict(X, theta):
    return np.dot(X, theta)

#Use gradient descent to optimise the model parameters

def gradient_descent(X, y, theta, learning_rate, iterations):
    m=len(y)
    for _ in range(iterations):
        error = np.dot(X, theta) - y
        gradient = (1/m) * np.dot(X.T, error)
        theta -=learning_rate * gradient
    return theta

#Calculate evaluation metrices

def mean_square_error(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

def r_squared(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred)**2)
    ss_tot=np.sum((y_true - np.mean(y_true))**2)
    return 1-(ss_res/ss_tot)

#Perform gradient descent and evaluations
optimised_theta = gradient_descent(X_b, y, theta, learning_rate, iterations)
y_pred = predict(X_b, optimised_theta)
mse = mean_square_error(y, y_pred)
r_squared= r_squared(y, y_pred)

print("Optimised Theta: ",optimised_theta)
print("Mean Squared Error: ",mse)
print("R squared: ",r_squared)

