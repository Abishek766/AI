from scipy.stats import ttest_1samp, ttest_ind, ttest_rel

#Perform one t- test
data = [10,12,15,16,17,18]
population_mean = 15
ttest_stats,p_value=ttest_1samp(data, population_mean)
print("T-Test One Sample: ",ttest_stats)

if(p_value <=0.05):
    print("Reject Null Hypothesis")
else:
    print("Fail to reject Null Hypothesis")


#Perform T-Test two sample
group1=[15,16,12,17,18]
group2=[13,17,16,11,12]

ttest_2, p_value1 = ttest_ind(group1,group2)
print("T-Test Two Sample: ",ttest_2)

if(p_value1 <=0.05):
    print("Reject Null Hypothesis")
else:
    print("Fail to reject Null Hypothesis")

#Perform Paired T-Test
pre_data=[15,16,12,17,18]
post_data=[19,17,14,18,20]
ttest,p_value = ttest_rel(pre_data,post_data)
print("T-Test Paired Sample: ",ttest_2)

if(p_value <=0.05):
    print("Reject Null Hypothesis")
else:
    print("Fail to reject Null Hypothesis")

