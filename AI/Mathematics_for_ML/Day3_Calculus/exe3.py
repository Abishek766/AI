import sympy as sp
import numpy as np

#Define the gradient descent function
def gradient_descent(x, y, theta, learning_rate, iterations):
    m=len(y)
    for _ in range(iterations):
        predications=np.dot(x, theta)
        errors = predications - y
        gradient= (1/m) * np.dot(x.T,errors)
        theta-= learning_rate * gradient
    return theta

#sample Data
x = np.array([[1,1],[1,2],[1,3]])
y=np.array([2, 2.5 ,3.5])
theta= np.array([0.1, 0.1])
learning_rate = 0.1
iterations = 1000

#gradient descent 
optimised_theta = gradient_descent(x, y, theta, learning_rate, iterations)
print("Optimised Parameters: ",optimised_theta)