import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = {
    'Age': [22,25,18,45,12,43,23,33],
    'Gender':['F','F','M','M','F','M','M','M'],
    'Smoker':['N','S','S','N','S','S','S','S'],
    'Disease':[1,1,0,0,0,1,0,1]
}

df = pd.DataFrame(data)

#Feature encoding
df = pd.get_dummies(df, columns=['Gender','Smoker'], dtype=int)
#print(df.head(5))

#Separate a features and target
X= df.drop('Disease', axis=1)
Y=df['Disease']

# print(X)

#Split the data into training and testing
X_train,X_test,y_train,y_test =train_test_split(X,Y)

#Fit the model
model = LogisticRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

#Finding coefficient and intercept
coefficient = model.coef_[0]
intercept = model.intercept_[0]

# print("Regression coefficient (m1,m2,m3,m4,m5)", coefficient)
# print("Intercept is: ", intercept)

#Test with out of box data
data1 = [[23,1,0,1,0]]
columns = ['Age', 'Gender_F', 'Gender_M', 'Smoker_N', 'Smoker_S']
df_new = pd.DataFrame(data1, columns=columns)

single = model.predict(df_new)
print(single)