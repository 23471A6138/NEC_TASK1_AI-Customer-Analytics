import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

data = pd.read_csv("dataset/customers.csv")

X = data[['AnnualIncome','SpendingScore']]

model = KMeans(
    n_clusters=3,
    random_state=42
)

model.fit(X)

data["Cluster"] = model.labels_

plt.figure(figsize=(8,6))

plt.scatter(
    data["AnnualIncome"],
    data["SpendingScore"],
    c=data["Cluster"],
    cmap="viridis",
    s=80
)

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.colorbar(label="Cluster")

plt.savefig(
    "static/charts/segmentation.png"
)

joblib.dump(
    model,
    "models/customer_segment.pkl"
)

print("Segmentation Model Saved")