import numpy as np
from scipy.stats import ttest_ind

#Sample data
group1=[22,25,24,26,21,29]
group2=[31,25,27,28,29,39]


#Perform P-Test
t_stat, p_value = ttest_ind(group1,group2)
print("T-Statistics: ", t_stat)
print("p_value: ",p_value)

#Interpret Result
alpha = 0.05

if p_value <= alpha:
    print("Reject Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")