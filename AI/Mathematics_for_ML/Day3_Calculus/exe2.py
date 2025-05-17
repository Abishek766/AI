import sympy as sp

#Define a multiveriable functions
x, y=sp.symbols('x y')
f= x**2 + 3*y**2 - 4*x*y

#Compute partial derivatives
grad_x= sp.diff(f,x)
grad_y= sp.diff(f,y)

print("Gradient:")
print("Grad X:",grad_x)
print("Grad Y:",grad_y)
