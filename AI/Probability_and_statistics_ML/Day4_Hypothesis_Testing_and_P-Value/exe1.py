import numpy as np
from scipy.stats import ttest_1samp

#Sample data
data =[12,16,17,18,19,14,15]

#Null Hypothesis: mean =15
population_mean = 15

#Perform P-Test
t_stat, p_value = ttest_1samp(data, population_mean)
print("T-Statistics: ", t_stat)
print("p_value: ",p_value)

#Interpret Result
alpha = 0.05

if p_value <= alpha:
    print("Reject Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")
