#Perfom Annova
from scipy.stats import f_oneway

group1=[22,25,24,26,21,29]
group2=[31,25,27,28,29,39]
group3=[10,11,20,19,14]

fsts,p_value = f_oneway(group1,group2,group3)
print("F-Statistics: ",fsts)
print("P-Value",p_value)