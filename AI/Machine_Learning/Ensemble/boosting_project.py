import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score, classification_report


#Load Dataset
url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(df.info())

#Feature selection
X=df[['Pclass','Name','Sex','Age','Fare','Embarked']]
y=df['Survived']

#Hanling missing values
df.fillna({'Age': df['Age'].median()}, inplace=True)
df.fillna({'Embarked': df['Embarked'].mode()[0]}, inplace=True)

#Feature encoding converting categorical data into numerical
X = pd.get_dummies(X, columns=['Name','Sex','Embarked'])

#Spliting the data into Training and testing
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

#Feature Scaling
sc = StandardScaler()
X_train_sc = sc.fit_transform(X_train)
X_test_sc = sc.transform(X_test)

#XGBoost
xgb = XGBClassifier()
xgb.fit(X_train_sc,y_train)
y_pred_xgb= xgb.predict(X_test_sc)

print("XGBoost Accuracy: ",accuracy_score(y_test,y_pred_xgb))
print("XGB (Classification Report): ", classification_report(y_test,y_pred_xgb))

#LightGBM
light = LGBMClassifier()
light.fit(X_train_sc,y_train)
y_pred_lgb = light.predict(X_test_sc)

print("LightGBM Accuracy: ",accuracy_score(y_test,y_pred_lgb))
print("LighhtGBM (Classification Report): ", classification_report(y_test,y_pred_lgb))

#CatBoost
cat = CatBoostClassifier(verbose=0)
cat.fit(X_train_sc,y_train)
y_pred_cat=cat.predict(X_test_sc)

print("CatBoost Accuracy: ",accuracy_score(y_test,y_pred_cat))
print("CatBoost (Classification Report): ", classification_report(y_test,y_pred_cat))

