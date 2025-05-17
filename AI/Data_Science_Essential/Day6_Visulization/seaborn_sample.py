import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data=np.random.rand(5,5)
sns.heatmap(data,annot=True,cmap='coolwarm')
plt.title("Heatmap")
plt.show()


