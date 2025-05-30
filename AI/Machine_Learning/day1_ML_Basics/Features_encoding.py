#url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df= pd.read_csv(url)
# print(df.info())
# print(df.sex.value_counts)
# print(df.sex.mode())

#Handling Missing Values
df['sex']=df['sex'].fillna('Male')

#Label Encoding
label_encoding = preprocessing.LabelEncoder()
df['sex_labels']=label_encoding.fit_transform(df.sex.values)

# print(df.head(5))

#One-Hot Encoding
one_hot = pd.get_dummies(df['day'], dtype=int)
print(one_hot)


#Dummy Encoding
dummy_encoding = pd.get_dummies(df['day'], drop_first=True, dtype=int)
print(dummy_encoding.head(5))