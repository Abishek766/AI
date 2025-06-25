import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler , LabelEncoder
# from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.naive_bayes import BernoulliNB
# from sklearn.svm import SVC
# from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report,confusion_matrix
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler

df = pd.read_csv(r"C:\Users\LENOVO\Downloads\WA_Fn-UseC_-Telco-Customer-Churn.csv")
# print(df.head(5))
# print(df.info())

#Data Preprocessing

#Data type error in total charger we need to convert to numerical values
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
# print(df.info())

#Handling missing values
#Total Charges have 11 missing values and its missing values is 0.15% which is less than 1% so , we get rid of them

df.dropna(how='any', inplace=True)

#Divide the data into Features and Target
X= df.drop(['customerID', 'Churn'], axis=1)
y = df.Churn.values

print(df.Churn.value_counts()/len(df)*100)
# print(X.columns)

#Feature Encoding--> Converting the categorical featuures to numerical
X = pd.get_dummies(X, columns=['gender', 'Partner', 'Dependents',
       'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
       'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
       'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod'],drop_first=True, dtype=int)

#Spliting the data into training and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

#Feature Scaling
sc = StandardScaler()
X_train_sc = sc.fit_transform(X_train)
X_test_sc = sc.transform(X_test)

# Here we noticed that
# No : 73 %
# yes : 26 %
# so it definitely leads to class imbalanced, we need rectify that
# Treating class imbalanced problem

#Over Sample
# over_sample = RandomOverSampler()
# X_train_sampled, y_train_sampled = over_sample.fit_resample(X_train_sc,y_train)
# model_dt = DecisionTreeClassifier()
# model_dt.fit(X_train_sampled,y_train_sampled)
# y_pred_dt = model_dt.predict(X_test_sc)

#Under Sample
under_sample = RandomUnderSampler()
X_train_undersample, y_train_undersample = under_sample.fit_resample(X_train_sc,y_train)

model_dt = DecisionTreeClassifier()
model_dt.fit(X_train_undersample,y_train_undersample)
y_pred_dt_u = model_dt.predict(X_test_sc)


print(classification_report(y_test,y_pred_dt_u))