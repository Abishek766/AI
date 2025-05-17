import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#load dataset
df= pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

del df['species']

#Calculate Correlation
correlation_matrix=df.corr()

#plot heatmap
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("Correlation heatmap")
plt.show()