import sympy as sp

#Define a function
x = sp.Symbol('x')
f = x**3 + 5*x - 7

#derivatives
derivative = sp.diff(f,x)
print("Function: ",f)
print("Derivatives: ",derivative)