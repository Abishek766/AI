#perform  chi square test
#obj: To test independence of two categorical varaiables

from scipy.stats import chi2_contingency

#Create Contigency Table
data = [[50,30,20],[30,40,30]]
chi2,p_value,dof,expected = chi2_contingency(data)
print("Chi2-Test: ",chi2)
print("P-Value: ",p_value)
print("Expected Frequencies: ",expected)