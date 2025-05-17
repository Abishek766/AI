import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm,binom,poisson,uniform

#Gaussian distribuition
x=np.linspace(-4,4,100)
plt.plot(x,norm.pdf(x,loc=0,scale=1),label="Gaussian (u=0, sigma=1)")

#Binomial Distribution
n,p=10,0.5
x=np.arange(0,n+1)
plt.bar(x, binom.pmf(x,n,p),alpha=0.7, label="Binomial (n=10), (p=0.5)")

#Poission Distribution
lam=3
x=np.arange(0,10)
plt.bar(x,poisson.pmf(x,lam),alpha=0.7, label="Poision (l=3)")

plt.title("Probability Distribution")
plt.legend()
plt.show()