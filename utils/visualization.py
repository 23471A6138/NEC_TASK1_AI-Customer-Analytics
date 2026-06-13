import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load dataset
data = pd.read_csv("dataset/customers.csv")

# Features for clustering
X = data[['AnnualIncome', 'SpendingScore']]

# K-Means
kmeans = KMeans(
    n_clusters=3,
    random_state=42
)

data['Cluster'] = kmeans.fit_predict(X)

# Scatter Plot
plt.figure(figsize=(8,6))

plt.scatter(
    data['AnnualIncome'],
    data['SpendingScore'],
    c=data['Cluster']
)

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")

# Save chart
plt.savefig(
    "static/charts/cluster.png"
)

plt.close()

print("Cluster Chart Saved!")