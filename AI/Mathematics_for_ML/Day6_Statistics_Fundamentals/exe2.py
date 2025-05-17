from scipy.stats import ttest_ind

#sample datasets
group1=[2.1, 2.5, 2.8, 3.2]
group2=[1.8, 2.0, 2.4, 2.7, 2.9]

#Perform t test
t_test, p_value = ttest_ind(group1,group2)

print("T-Statistice: ",t_test)
print("P Value: ",p_value)

#Interpretation

#set statistics significant 
alpha = 0.05
if alpha > p_value:
    print("Reject Null Hypothesis: significant difference")
else:
    print("Null Hypothesis: no significant difference")
