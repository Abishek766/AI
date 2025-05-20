from scipy.stats import chi2_contingency
from scipy.stats import f_oneway

#Contigency Table
# data = [[50, 30],[20,40]]

# #Perform Chi-Square Test
# chi2, p,dof, expected = chi2_contingency(data)
# print("Chi-Square Statistice,: ",chi2)
# print("P-Value: ",p)
# print(dof)
# print("Expected Frequencies: \n",expected)

#Perform Annova test
group1=[15,16,12,17,18]
group2=[13,17,16,11,12]
group3=[10,11,20,19,14]

f_stats, p_value=f_oneway(group1,group2,group3)
print("F-Statistice: ",f_stats)
print("P-Value",p_value)

if(p_value <= 0.05):
    print("Reject Null Hypothesis: Atleast One group is different")
else:
    print("Failed to Reject Null Hypothesis: All groups are same")