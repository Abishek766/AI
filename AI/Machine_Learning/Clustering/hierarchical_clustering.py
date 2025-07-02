import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.cluster import hierarchy as sch #--> it is used to create dendrogram
from sklearn.cluster import AgglomerativeClustering

df=pd.read_excel(r"C:\Users\LENOVO\OneDrive\Desktop\Mall_Customers.xlsx")

#Features
X = df[['Annual Income (k$)','Spending Score (1-100)']].values

#Using dendrogram to find number of clusters
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
plt.title('Dendrograms')
plt.xlabel('Customers')
plt.ylabel('Spending')
plt.show()

plt.close()

#As per hierarchical clustering we have 4 clusters references in diagram

#Applying Hierarchical clustering
hc = AgglomerativeClustering(n_clusters=4, linkage='ward')
y_hc=hc.fit_predict(X)

#Visualizing the clusters
plt.scatter(X[y_hc == 0,0], X[y_hc == 0,1], s=100, c='red', label='Cluster1')
plt.scatter(X[y_hc == 1,0], X[y_hc == 1,1], s=100, c='blue', label='Cluster2')
plt.scatter(X[y_hc == 2,0], X[y_hc== 2,1], s=100, c='green', label='Cluster3')
plt.scatter(X[y_hc == 3,0], X[y_hc == 3,1], s=100, c='yellow', label='Cluster4')


plt.title("Cluster of Clients")
plt.xlabel("Annual Income")
plt.ylabel("Spending")
plt.legend()
plt.show()


