import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler , LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

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

# #Fit the model
# model = KNeighborsClassifier()
# model.fit(X_train_sc,y_train)
# y_pred = model.predict(X_test_sc)

# # Model Evalution
# accuracy = round(accuracy_score(y_test,y_pred)*100,2)
# print(accuracy)

#Fit the model
model_dt = DecisionTreeClassifier()
model_dt.fit(X_train_sc,y_train)
y_pred = model_dt.predict(X_test_sc)

# Model Evalution
accuracy = round(accuracy_score(y_test,y_pred)*100,2)
print(accuracy)