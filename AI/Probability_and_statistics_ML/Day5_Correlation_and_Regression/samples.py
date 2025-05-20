import numpy as np
from scipy.stats import pearsonr, spearmanr

#Sample dataset
x=np.array([1, 2, 3, 4, 5])
y=np.array([2, 4, 6, 8, 10])

#Perform Correlation
r, p_value = pearsonr(x,y)
print("Pearsonr Correlation Coefficent: ",r)
print("P-Value: ",p_value)

#Perform spearmanr
p , p_value = spearmanr(x,y)
print("Spearmanr Correlation Coefficient: ",p)
print("P-Value: ",p_value)