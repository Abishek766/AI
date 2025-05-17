import sympy as sp

#f(x)= (x^2)
#f'(x) = 2x
# x = sp.Symbol('X')
# f=x **2
# Derivative=sp.diff(f,x)
# print(Derivative)

#f(x) = sin(x)
#f'(x) = cos(x)

# x = sp.Symbol('x')
# f = sp.sin(x)
# derivate = sp.diff(f,x)
# print(derivate)

#Partial derivates and gradients

x, y= sp.symbols('x y')
f=x**2 + y**2

#Partial derivates
df_dx = sp.diff(f,x) 
df_dy = sp.diff(f,y)

#Gradient
gradient=[df_dx,df_dy]

print("Partial derivates: ",df_dx,df_dy)
print("Gradient: ",gradient)
