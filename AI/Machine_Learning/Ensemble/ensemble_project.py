import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler , LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report,confusion_matrix
from xgboost import XGBClassifier

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

label_encoding = LabelEncoder()
y = label_encoding.fit_transform(y)

#Spliting the data into training and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

#Feature Scaling
sc = StandardScaler()
X_train_sc = sc.fit_transform(X_train)
X_test_sc = sc.transform(X_test)

#AdaBoost
model_ada = AdaBoostClassifier(n_estimators=200)
model_ada.fit(X_train_sc, y_train)
y_pred_ada = model_ada.predict(X_test_sc)

print("Accuracy of Ada Boost: ", accuracy_score(y_test,y_pred_ada))

#GradientBoost
model_gradient = GradientBoostingClassifier(n_estimators=200)
model_gradient.fit(X_train_sc,y_train)
y_pred_gb = model_gradient.predict(X_test_sc)

print("Accuracy of gradient Boost: ", accuracy_score(y_test,y_pred_gb))

#XGBoost
xgb = XGBClassifier(n_estimators=200)
xgb.fit(X_train_sc,y_train)
y_pred_xgb = xgb.predict(X_test_sc)
print("Accuracy of XG Boost: ", accuracy_score(y_test,y_pred_xgb))