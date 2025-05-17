# Bernoulli  Distribution which describes outcomes of a binary experiment
# P(X = 1)=p, P(X = 0)= 1-p

import numpy as np
import matplotlib.pyplot as plt

p=0.6
plt.bar([0,1],[1-p,p], color="blue")
plt.title("Bernoulli Distribution")
plt.xticks([0,1],labels=["0 (failures)","1 (success)"])
plt.show()