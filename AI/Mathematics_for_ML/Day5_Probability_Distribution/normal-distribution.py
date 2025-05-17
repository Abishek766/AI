import numpy as np
import matplotlib.pyplot as plt

mu,sigma = 0,1
x=np.linspace(-4,4,100)
y=(1/(np.sqrt(2*np.pi*sigma**2)))*np.exp(-0.5 * ((x - mu)/sigma)**2)

plt.plot(x,y)
plt.title("Gaussian Distribution")
plt.show()