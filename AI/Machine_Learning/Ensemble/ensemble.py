import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

#Create dataset
X, y = make_classification(n_samples=10000, n_features=10, n_informative=3 , random_state=42)

X_train, X_test, y_train , y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Feature Scaling
sc = StandardScaler()
X_train_sc = sc.fit_transform(X_train)
X_test_sc = sc.transform(X_test)

#Decision Tree
model_dt = DecisionTreeClassifier()
model_dt.fit(X_train_sc,y_train)
y_pred_dt = model_dt.predict(X_test_sc)

print("Decision Tree Accuracy: ",round(accuracy_score(y_test,y_pred_dt)*100,2))

#Bagging (Decision Tree)
bag_dt = BaggingClassifier(estimator=DecisionTreeClassifier(), 
                           n_estimators=500, 
                           max_samples=0.50, 
                           bootstrap= True, random_state=42)
bag_dt.fit(X_train_sc,y_train)
y_pred_bagdt = bag_dt.predict(X_test_sc)

print("Bagging Classifier Accuracy(Decision Tree): ",round(accuracy_score(y_test,y_pred_bagdt)*100,2))

#Random Forest
rf = RandomForestClassifier(n_estimators=500)
rf.fit(X_train_sc,y_train)
y_pred_rf = rf.predict(X_test_sc)

print("Random Forest Accuracy: ",round(accuracy_score(y_test,y_pred_rf)*100,2))

#Bagging (SVM)
bag_svm = BaggingClassifier(estimator=SVC(), 
                           n_estimators=500, 
                           max_samples=0.25, 
                           bootstrap= True, random_state=42)
bag_svm.fit(X_train_sc,y_train)
y_pred_svm = bag_svm.predict(X_test_sc)

print("Bagging Classifier Accuracy(SVM): ",round(accuracy_score(y_test,y_pred_svm)*100,2))

#Pasting
pasting = BaggingClassifier(estimator=DecisionTreeClassifier(), 
                           n_estimators=500, 
                           max_samples=0.50, 
                           bootstrap= False, random_state=42)
pasting.fit(X_train_sc,y_train)
y_pred_pas = pasting.predict(X_test_sc)

print("Pasting Accuracy: ",round(accuracy_score(y_test,y_pred_pas)*100,2))


