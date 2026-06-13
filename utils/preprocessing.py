import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(file_path):

    data = pd.read_csv(file_path)

    data = data.dropna()

    scaler = StandardScaler()

    data[['Age','AnnualIncome','SpendingScore']] = scaler.fit_transform(
        data[['Age','AnnualIncome','SpendingScore']]
    )

    return data