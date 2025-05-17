import sympy as sp

#Define a function
x = sp.Symbol('x')
f = sp.exp(-x)

#Compute Integrals
indefinite = sp.integrate(f,x)
definite = sp.integrate(f, (x,0,sp.oo))

print("In-Definite: ",indefinite)
print("Definite: ",definite)