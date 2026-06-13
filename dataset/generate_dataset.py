import pandas as pd
import random

data = []

for i in range(1, 101):
    age = random.randint(18, 60)
    gender = random.choice(["Male", "Female"])
    income = random.randint(20000, 100000)
    score = random.randint(1, 100)

    purchased = 1 if score > 50 else 0

    data.append([
        i,
        age,
        gender,
        income,
        score,
        purchased
    ])

df = pd.DataFrame(
    data,
    columns=[
        "CustomerID",
        "Age",
        "Gender",
        "AnnualIncome",
        "SpendingScore",
        "Purchased"
    ]
)

df.to_csv(
    "dataset/customers.csv",
    index=False
)

print("100 Customer Dataset Created!")