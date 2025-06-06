#url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

#Define Features and Target
feature = df[['total_bill','size']]
target = df['tip']

print("Features: \n",feature.head())
print("Target:  \n",target.head())

#Training and testing Dataset
X_train,X_test,y_train,y_test=train_test_split(feature, target, test_size=0.2, random_state=42)
print("Traning Data Set: ",X_train.shape)
print("Testing Data Set: ",X_test.shape)

#Visualizing Dataset
sns.pairplot(df, x_vars=['total_bill','size'], y_vars='tip',height=5,aspect=0.8, kind='scatter')
plt.title("Features vs Target")
plt.show()
