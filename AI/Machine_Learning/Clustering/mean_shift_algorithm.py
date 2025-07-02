import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift

df=pd.read_excel(r"C:\Users\LENOVO\OneDrive\Desktop\Mall_Customers.xlsx")

#Features
X = df[['Annual Income (k$)','Spending Score (1-100)']].values

#Fitting the Mean Shift Algorithm
ms = MeanShift(bandwidth=20)
#Adjusting the bandwidth parameters to influence the number of clusters

ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_

print(labels)

#Visualizing the clusters
n_clusters = len(np.unique(labels))
colors = ['red','blue','green','yellow','cyan','purple','pink']

for i in range(n_clusters):
    cluster = X[labels == i]
    plt.scatter(cluster[:,0], cluster[:,1],s=100,c=colors[i], label=f"Cluster {i+1}")

plt.title("Cluster of Clients")
plt.xlabel("Annual Income")
plt.ylabel("Spending")
plt.legend()
plt.show()
