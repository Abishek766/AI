# "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

from scipy.stats import skew,kurtosis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load dataset
df=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
feature = df["sepal_length"]
print("Skewness: ",skew(feature))
print("Kurtosis: ",kurtosis(feature))


#Visulize
sns.histplot(feature,kde=True)
plt.title("Distribution of Sepal Length")
plt.show()


