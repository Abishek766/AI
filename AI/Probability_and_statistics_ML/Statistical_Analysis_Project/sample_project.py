import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind,chi2_contingency
from sklearn.linear_model import LinearRegression

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

df= pd.read_csv(url)

#Inspect data
print(df.info())
print(df.describe())

#Visulise Distribution
sns.histplot(df["total_bill"], kde=True)
plt.title("Distribution of Total Bill")
plt.show()

#Conducting Hypothesis test

#Separate data by gender
male_tips = df[df["sex"]== 'Male']['tip']
female_tips = df[df["sex"]== 'Female']['tip']

#Perform t-test
ttest_sts, p_value=ttest_ind(male_tips,female_tips)
print("T-Statistics: ",ttest_sts)
print("P-Value: ",p_value)

#Interpret results
alpha =0.05
if(p_value <=alpha):
    print("Reject all Null Hypothesis: Significant difference")
else:
    print("Failes to Reject Null Hypothesis")


#Perform Chi2 test
contingency_table = pd.crosstab(df["smoker"],df['time'])

chi2, p_value, dof, expected = chi2_contingency(contingency_table)
print("Chi2 Statistice: ",chi2)
print("P-Value: ",p_value)

if(p_value<=0.05):
    print("Reject Null Hypothesis: The Two variables are dependent each other")
else:
    print("Failed to Reject Null Hypothesis: Independent Each Other")



#Applying Linear Regression for total bill and tip
x = df["total_bill"].values.reshape(-1,1)
y = df["tip"].values

#Fit Linear Regression
model = LinearRegression()
model.fit(x,y)

#Output Coefficient
print("Slope: ",model.coef_[0])
print("Intercept: ",model.intercept_)
print("R-Squared: ",model.score(x,y))

#Plot regression
sns.scatterplot(x=df["total_bill"], y=df["tip"], color="blue")
plt.plot(df["total_bill"], model.predict(x), color="red", label="Linear Regression")
plt.title("Total Bill vs Tip")
plt.show()