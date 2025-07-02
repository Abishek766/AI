import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

df=pd.read_excel(r"C:\Users\LENOVO\OneDrive\Desktop\Mall_Customers.xlsx")
# print(df.head(5))

#Features
X = df[['Annual Income (k$)','Spending Score (1-100)']].values

# Set K-values using Elbow method
wcss=[]
for i in range(1,11): # Run through loop for 10 clusters
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_) #inertia -> sum of squared values 

#Visulization
# plt.plot(range(1,11),wcss)
# plt.title("Elbow Method")
# plt.xlabel("Cluster")
# plt.ylabel("WCSS")
# plt.show()

#K = 5

#Applying k-means algorithms
kmeans = KMeans(n_clusters=5)
y_kmeans = kmeans.fit_predict(X)

#Visulizing the clusters
plt.scatter(X[y_kmeans == 0,0], X[y_kmeans == 0,1], s=100, c='red', label='Cluster1')
plt.scatter(X[y_kmeans == 1,0], X[y_kmeans == 1,1], s=100, c='blue', label='Cluster2')
plt.scatter(X[y_kmeans == 2,0], X[y_kmeans == 2,1], s=100, c='green', label='Cluster3')
plt.scatter(X[y_kmeans == 3,0], X[y_kmeans == 3,1], s=100, c='yellow', label='Cluster4')
plt.scatter(X[y_kmeans == 4,0], X[y_kmeans == 4,1], s=100, c='violet', label='Cluster5')

plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=300, c='black', label='Centriod')
plt.title("Cluster of Clients")
plt.xlabel("Annual Income")
plt.ylabel("Spending")
plt.legend()
plt.show()
